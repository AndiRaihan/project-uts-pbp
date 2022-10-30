
var nameList = [];

var urlRegex = /^[A-Za-z0-9-]*$/;


function validate_input(id) {
    var element = document.getElementById(id);

    if (urlRegex.test(element.value) && element.value != "") {
        element.reportValidity();
        element.setCustomValidity('');
    }
    if (!element.checkValidity()) {
        $("#feedback-url").show();
        $("#feedback-exist").hide();
    } else if (nameList.includes(element.value)) {
        // Hide invalide msg ke-1
        $("#feedback-url").hide();
        // Show invalid msg ke-2
        $("#feedback-exist").show();
        element.setCustomValidity("Nama sudah ada.");
    }
    else {
        element.setCustomValidity('');
        // Show invalid msg ke-1
        $("#feedback-url").hide();
        $("#feedback-exist").hide();

    }

}


$(document).ready(function () {
    $("#feedback-exist").hide();
    $.ajax({
        url: './name',
        dataType: 'json',
        success: function (data) {
            for (var i = 0; i < data.name_list.length; i++){
                nameList[i] = data.name_list[i][0];
            }
        },
    });

    (() => {
        'use strict'

        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        const forms = document.querySelectorAll('.needs-validation')

        // Loop over them and prevent submission
        Array.from(forms).forEach(form => {
            form.addEventListener('submit', event => {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }
                $("#id_forum_name").on('input', function (e) {
                    validate_input("id_forum_name");
                });
                form.classList.add('was-validated')
            }, false)
        })
    })()
});