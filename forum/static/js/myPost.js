var url = window.location.href
function upvote(id) {
    $.ajax({
        url: `./${id}/upvote`,
        datatype: 'json',
        success: function (data) {
            $(`#upvote${id}`).html(`&#128316 Upvote ${data.upvote}`);
        }
    });
}

function editPost() {
    var name = $('#id_title').val();
    var description = $(`#id_description`).val();
    var is_captured = false;
    var idPost = $('#id_id_post').val();
    if ($('#id_checkbox').is(":checked")) {
        is_captured = true;
    }
    // YYYY-MM-DD
    var captured_date = $('#id_capture_date').val();
        console.log(captured_date);
        console.log(is_captured);
        $.ajax({
            type: 'POST',
            url: `${url}${idPost}/edit/`,
            data: {
                name: name,
                description: description,
                is_captured: is_captured,
                date_captured: captured_date,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                id: idPost,
            },
            success: function (data) {
                console.log(data.msg);
                if (data.msg === 'fail') {
                    if (!$('#form-edit-post').hasClass('was-validated')) {
                        $('#form-edit-post').addClass('was-validated');
                    }
                } else {
                    console.log("Masuk else");
                    // TODO Edit Html DOM-nya
                    resetForm()
                }
            }, error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });

}


function resetForm() {
    $('#form-edit-post').trigger("reset");
    $('#form-edit-post').removeClass('was-validated')
    $('#input-date').addClass('d-none');
}

$(document).ready(function () {
    $(".multiple-select").chosen({ width: "100%" });
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
            }, false)
        })
    })()
    var test = `<p>Test sesuatu</p>`;
    $('#placeholder').append(test);
});