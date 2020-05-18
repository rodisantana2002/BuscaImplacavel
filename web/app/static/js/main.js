$(document).ready(function () {
   var url_base = "http://localhost:5000/";
   var url_files_txt = "static/files/txt/"
   var url_files_bib = "static/files/bib/"

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

    // $('#card-estatistica-bibtext').hide();

    // Carregar BibText
    $('#btn-bibtext-carregar').click(function (){
                
        if (validarDadosFileBib()) {
            var dialog = bootbox.dialog({
                title: 'Atenção!',
                message: '<div class="text-center"><i class="fa fa-spin fa-spinner"></i>Aguarde... processando arquivo...</div>',
                closeButton:true,
                centerVertical: true
            });

            dialog.init(function () {
                setTimeout(function () {
                    // carrega conteudo do arquivo selecionado
                    jQuery.get(url_base + url_files_bib + $("#name-file-bibtext").val().split('\\').pop(),
                        function (data) {
                            conteudo = data;
                            $.ajax({
                                type: "POST",
                                url: url_base + "referencia/importar/file",
                                data: {
                                    bibText: conteudo
                                },
                                async: true,
                                success: function (data) {
                                    $(location).attr('href', url_base + 'referencia/import/')
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
                size: 'small',
                centerVertical:true
            });          
            $("#name-file-bibtext").focus();
        }
    });


// ---------------------------------------------------------


    // registrar processo
    $("#btn-processo-enviar").click(function () {
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

    // remover processo
    $(".btn-processo-remover").click(function (){
        var processo = jQuery.parseJSON($(this).val());
        
        bootbox.confirm({
            message: "Confirma a remoção do Processo?",
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
                    var dialog = bootbox.dialog({
                        message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> Aguarde... processando exclusão...</p>',
                        centerVertical: true,
                        closeButton: true
                    });

                    dialog.init(function () {
                        setTimeout(function () {
                        //processa a exlusão dos dados do processo
                            $.ajax({
                                type: "POST",
                                data: { id: processo.id },
                                url: url_base + "processo/remover",
                                async: true,
                                success: function (data) {
                                    if (data === "200") {
                                        location.reload();
                                    }
                                    else {
                                        dialog.find('.bootbox-body').html("Não foi possível excluir o registro!");
                                    }
                                }
                            });

                        }, 1);
                    });

                }
            }
        });    

    });

    // adicionar arquivo ao processo
    $("#btn-arquivo-adicionar").click(function () {
        var processo = jQuery.parseJSON($(this).val());

        if (validarDadosFile()) {
            var dialog = bootbox.dialog({
                title: 'Atenção!',
                message: '<div class="text-center"><i class="fa fa-spin fa-spinner"></i>Aguarde... processando arquivo...</div>',
                closeButton:true,
                centerVertical: true
            });

            dialog.init(function () {
                setTimeout(function () {
                    // carrega conteudo do arquivo selecionado
                    jQuery.get(url_base + url_files_txt + $("#name-file").val().split('\\').pop(),
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
                size: 'small',
                centerVertical:true
            });          
            $("#name-file").focus();
        }
    });

    //processamento da busca online das referencias
    $(".btn-arquivo-processar").click(function (){
        var file = jQuery.parseJSON($(this).val());
        
        if (file.pendentes>0){
            var dialog = bootbox.dialog({
                title: 'Atenção!',
                message: '<div class="text-center"><i class="fa fa-spin fa-spinner fa-2x"></i><br>Aguarde... atualizando referências <br> Tempo Estimado [ ' + file.tempo + ' ]</div>',
                closeButton: true,
                centerVertical: true
            });
    
            dialog.init(function () {
                setTimeout(function () {
                    $.ajax({
                        type: "POST",
                        data: { id: file.id },
                        url: url_base + "processo/arquivo/processar",
                        async: true,
                        success: function (data) {
                            if (data === "200") {
                                location.reload();
                            }
                            else {
                                dialog.find('.bootbox-body').html("Não foi possível processar o arquivo");
                            }
                        }
                    });                    
    
                }, 1);
            });
    
        }
        else{
            bootbox.alert({
                message: "Não existem referências para serem processadas!",
                size: 'large',
                centerVertical:true
            }); 
        }

    });     


    // processa a remoção do arquivo selecionado
    $(".btn-arquivo-remover").click(function () {
        var file = jQuery.parseJSON($(this).val());

        bootbox.confirm({
            message: "Confirma a remoção do Arquivo?",
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
                        url: url_base + "processo/arquivo/remover",
                        async: false,
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
    
    // exibe popup com detalhes da referencia
    $(".btn-referencia-detail").click(function () {
        var referencia = jQuery.parseJSON($(this).val());
        bootbox.alert({
            message: "<p> lin.: " + referencia.linha + "</p>" +
                "<p> ref.: " + referencia.referencia + "</p>",
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
                        url: url_base + "processo/arquivo/referencia/remover",
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

    // valida dados arquivo upload - bibText
    function validarDadosFileBib() {
        if ($("#name-file-bibtext").val().trim().length === 0) {
            return false;
        }
        return true;
    }
});
