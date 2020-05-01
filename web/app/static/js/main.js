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
    $("#btn-adicionar-arquivo").click(function () {
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
    
    $(".btn-referencia-processar").click(function (){
        var file = jQuery.parseJSON($(this).val());        
        alert(file.id);

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
