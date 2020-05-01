$(document).ready(function () {
   var url_base = "http://localhost:5000/";
   var url_files_import = "static/files/import/"
   var url_files_export = "static/files/export/"

    // exibe alerta regsitro
    if ($("#registro-alerta").html() === "") {
        $("#registro-alerta").hide();
    } else {
        $("#registro-alerta").show();
    };

    $('table.display').DataTable({      
        "displayLength": 5
    });

    $('#dataTableProcessos').DataTable({
        "order":[[4, "desc"]]
    });
    
    $('.custom-file-input').on('change', function () {
        let fileName = $(this).val().split('\\').pop();
        $(this).next('.custom-file-label').addClass("selected").html(fileName);
    });


    // registrar processo
    $("#btn-enviar-processo").click(function () {
        if (validarDadosProcesso()) {
            $.ajax({
                type: "POST",
                url: url_base + "processo/registro",
                data: {
                    descricao: $("#descricao").val(),
                    objetivo: $("#objetivo").val()
                },
                async: false,
                success: function (data) {
                    $(location).attr('href', url_base + 'processo');
                }
            });
        }
    });    

    // adicionar arquivo ao processo
    $("#btn-arquivo-adicionar").click(function () {
        var processo = jQuery.parseJSON($(this).val());

        if (validarDadosFile()) {
            var dialog = bootbox.dialog({
                title: 'Atenção!',
                message: '<div class="text-center"><i class="fa fa-spin fa-spinner"></i>Aguarde processando arquivo...</div>',
                centerVertical: true
            });

            dialog.init(function () {
                setTimeout(function () {
                    // carrega conteudo do arquivo selecionado
                    jQuery.get(url_base + url_files_import + $("#name-file").val().split('\\').pop(),
                        function (data) {
                            conteudo = data;
                            $.ajax({
                                type: "POST",
                                url: url_base + "processo/arquivo",
                                data: {
                                    name_file: $("#name-file").val().split('\\').pop().toLowerCase(),
                                    processo_id: processo.id,
                                    conteudo: conteudo
                                },
                                async: true,
                                success: function (data) {                                   
                                    if (data === "200") {
                                        $(location).attr('href', url_base + 'processo/' + processo.id);
                                    }
                                    else{
                                        dialog.find('.bootbox-body').html("Arquivo já esta registrado no processo!");
                                    }
                                }
                            });
                        }
                    );            
                    
                }, 1);
            });
            
        }    
        else {
            bootbox.alert({
                message: "Selecione um arquivo",
                size: 'small'
            });          
            $("#name-file").focus();
        }
    });

    // processa a remoção do arquivo selecionado
    $(".btn-arquivo-remover").click(function () {
        var file = jQuery.parseJSON($(this).val());

        bootbox.confirm({
            message: "Confirma a remoção da Arquivo?",
            size: "small",
            centerVertical: true,
            buttons: {
                confirm: {
                    label: 'Sim',
                    label: '<i class="fa fa-check"></i> Confirm',
                    className: 'btn-success'
                },
                cancel: {
                    label: 'Não',
                    label: '<i class="fa fa-times"></i> Cancel',
                    className: 'btn-danger'
                }
            },
            callback: function (result) {
                if (result) {
                    $.ajax({
                        type: "POST",
                        data: { id: file.id },
                        url: url_base + "/processo/arquivo/remover",
                        async: true,
                        success: function (data) {
                            if (data === "200") {
                                location.reload();
                            }
                            else{    
                                bootbox.alert({
                                    message: "Não foi possível excluir o registro",
                                    size: 'small'
                                });
                            }                            
                        }
                    });                    
                }
            }
        });           

    });

    // processa a busca pelas referencias do arquivo selecionado
    $(".btn-arquivo-processar").click(function () {
        var file = jQuery.parseJSON($(this).val());
        alert(file.id);

    });

    // processa a exportação das referencias do arquivo selecionado
    $(".btn-arquivo-exportar").click(function () {
        var file = jQuery.parseJSON($(this).val());
        alert(file.id);
    });
    
    // exibe popup com detalhes da referencia
    $(".btn-referencia-detail").click(function () {
        var referencia = jQuery.parseJSON($(this).val());
        bootbox.alert({
            message: "<p> lin.: " + referencia.linha + "</p>" +
                "<p> ref.: " + referencia.referencia + "</p>" +
                "<p> bib.: " + referencia.bibtext + "</p>",
            size: 'large',
            centerVertical: true
        });
    });

    // exclusão individual da referencia
    $(".btn-referencia-remove").click(function (){
        var referencia = jQuery.parseJSON($(this).val());        

        bootbox.confirm({
            message: "Confirma a remoção da Referência?",
            size: "small",
            centerVertical: true,
            buttons: {
                confirm: {
                    label: 'Sim',
                    label: '<i class="fa fa-check"></i> Confirm',
                    className: 'btn-success'
                },
                cancel: {
                    label: 'Não',
                    label: '<i class="fa fa-times"></i> Cancel',
                    className: 'btn-danger'
                }
            },
            callback: function (result) {
                if (result) {
                    $.ajax({
                        type: "POST",
                        data: { id: referencia.id },
                        url: url_base + "/processo/arquivo/referencia",
                        async: false,
                        success: function (data) {
                            if (data !="200"){
                                bootbox.alert({
                                    message: "Não foi possível excluir o registro",
                                    size: 'small'
                                });  
                            }                            
                        }
                    });
                    location.reload();
                }
            }
        });        

    });


    // **********************************************************************************************
    // FUNÇÔES
    // **********************************************************************************************
    // valida dados formulario processo
    function validarDadosProcesso() {
        var msg = "O campo deve ser informado!"

        if ($("#descricao").val().trim().length === 0) {
            $("#registro-alerta").html(msg);
            $("#registro-alerta").show();
            $("#descricao").focus();
            return false;
        }

        if ($("#objetivo").val().trim().length == 0) {
            $("#registro-alerta").html(msg);
            $("#registro-alerta").show();
            $("#objetivo").focus();
            return false;
        }

        return true;
    }

    // valida dados arquivo upload
    function validarDadosFile() {
        if ($("#name-file").val().trim().length === 0) {
            return false;
        }
        return true;
    }
});
