$(document).ready(function () {
   var url_base = "http://localhost:5000/";

    $('#dataTable').DataTable({
        "order":[[4, "desc"]]
    });


    // exibe alerta regsitro
    if ($("#registro-alerta").html() === "") {
        $("#registro-alerta").hide();
    } else {
        $("#registro-alerta").show();
    };

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
});
