var nameList = []

var urlRegex = /^[A-Za-z0-9-]*$/

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
    $.ajax({
        url: './name',
        dataType: 'json',
        success: function (data) {
            nameList = data.name_list;
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
                    $("#feedback-exist").hide();
                    validate_input("id_forum_name");
                });
                form.classList.add('was-validated')
            }, false)
        })
    })()
});