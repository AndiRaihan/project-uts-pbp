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

function deletePost(id) {
    $.ajax({
        url: `./${id}/delete`,
        datatype: 'json',
        success: function (data) {
            $(`#card${id}`).remove();
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
        success: function (post) {
            if (post.msg === 'fail') {
                if (!$('#form-edit-post').hasClass('was-validated')) {
                    $('#form-edit-post').addClass('was-validated');
                }
            } else {
                console.log("Masuk else");
                // TODO Edit Html DOM-nya
                if (post.is_captured) {
                    $(`#card${post.id}`).css("border-color", "#DA0037");
                    $(`#card${post.id}`).empty();
                    var card = `<div class="card-header" style="background-color:white;">
                            <div class="row">
                                <div class="col-md-9">
                                    <h2 class="card-title">${post.title}</h2>
                                </div>
                                <div class="col-md">
                                    <div class="dropdown text-end">
                                        <a href="#" class="d-block link-dark text-decoration-none" data-bs-toggle="dropdown"
                                            aria-expanded="false" onclick="$('#id_id_post').val('${post.id}')">
                                            <i class="bi bi-three-dots-vertical" alt="mdo" width="35" height="35"
                                                class="rounded-circle"></i>
                                        </a>
                                        <ul class="dropdown-menu text-small">
                                            <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                                    data-bs-target="#modalTambahTask">Edit</a></li>
                                            <li>
                                                <hr class="dropdown-divider">
                                            </li>
                                            <li><a onclick="deletePost(${post.id});" class="dropdown-item" href="#">Delete</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <p class="card-text">Written by: Anonymous #${post.creator_id}</p>
                            <p class="card-text">${post.date_created}
                        </div>
                        <div class="card-body">
                            <p class="card-text">${post.description}</p>
            
                            <p class="card-text">Tanggal tertankap${post.date_captured}</p>
                            <br>
                            <button class="btn btn-upvote" onclick="upvote('${post.id}');" id="upvote${post.id}">&#128316 Upvote
                                ${post.upvote_count}</button>
                            <a href="${url}${post.id}/comment" class="btn-reply">&#128488 Reply</a>
                            <br>
                        </div>
                    </div>`;
                    $(`#card${post.id}`).append(card);
                } else {
                    $(`#card${post.id}`).css("border-color", "white")
                    $(`#card${post.id}`).empty();
                    var card = `<div class="card-header" style="background-color:white;">
                            <div class="row">
                                <div class="col-md-9">
                                    <h2 class="card-title">${post.title}</h2>
                                </div>
                                <div class="col-md">
                                    <div class="dropdown text-end">
                                        <a href="#" class="d-block link-dark text-decoration-none" data-bs-toggle="dropdown"
                                            aria-expanded="false" onclick="$('#id_id_post').val('${post.id}')">
                                            <i class="bi bi-three-dots-vertical" alt="mdo" width="35" height="35"
                                                class="rounded-circle"></i>
                                        </a>
                                        <ul class="dropdown-menu text-small">
                                            <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                                    data-bs-target="#modalTambahTask">Edit</a></li>
                                            <li>
                                                <hr class="dropdown-divider">
                                            </li>
                                            <li><a onclick="deletePost(${post.id});" class="dropdown-item" href="#">Delete</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <p class="card-text">Written by: Anonymous #${post.creator_id}</p>
                            <p class="card-text">${post.date_created}
                        </div>
                        <div class="card-body">
                            <p class="card-text">${post.description}</p>
                            <button class="btn btn-upvote" onclick="upvote('${post.id}');" id="upvote${post.id}">&#128316 Upvote
                                ${post.upvote_count}</button>
                            <a href="${url}${post.id}/comment" class="btn-reply">&#128488 Reply</a>
                            <br>
                        </div>
                    </div>`;
                    $(`#card${post.id}`).append(card);
                }
                resetForm();
            }
        }, error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });

}

function resetPost() {
    console.log("Masuk");
    $(`#my-post`).empty();
    $.ajax({
        url: `./json`,
        dataType: 'json',
        success: function (data) {
            for (var i = 0; i < data.length; i++) {
                if (data[i].fields.is_captured) {
                    var card = `<div id="card${data[i].pk}" class="card" style="width: 20rem; border-color: #DA0037;">
                    <div class="card-header" style="background-color:white;">
                        <div class="row">
                            <div class="col-md-9">
                                <h2 class="card-title">${data[i].fields.title}</h2>
                            </div>
                            <div class="col-md">
                                <div class="dropdown text-end">
                                    <a href="#" class="d-block link-dark text-decoration-none" data-bs-toggle="dropdown"
                                        aria-expanded="false" onclick="$('#id_id_post').val('${data[i].pk}')">
                                        <i class="bi bi-three-dots-vertical" alt="mdo" width="35" height="35"
                                            class="rounded-circle"></i>
                                    </a>
                                    <ul class="dropdown-menu text-small">
                                        <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                                data-bs-target="#modalTambahTask">Edit</a></li>
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                        <li><a onclick="deletePost(${data[i].pk});" class="dropdown-item" href="#>Delete</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <p class="card-text">Written by: Anonymous #${data[i].fields.creator}</p>
                        <p class="card-text">${data[i].fields.date_created}
                    </div>
                    <div class="card-body">
                        <p class="card-text">${data[i].fields.description}</p>
        
                        <p class="card-text">Tanggal tertankap${data[i].fields.date_captured}</p>
                        <br>
                        <button class="btn btn-upvote" onclick="upvote('${data[i].pk}');" id="upvote${data[i].pk}">&#128316 Upvote
                            ${data[i].fields.upvote_count}</button>
                        <a href="${url}${data[i].pk}/comment" class="btn-reply">&#128488 Reply</a>
                        <br>
                    </div>
                </div>`;
                    $(`#my-post`).append(card);
                } else {
                    var card = `<div id="card${data[i].pk}" class="card" style="width: 20rem;border-color: white;">
                    <div class="card-header" style="background-color:white;">
                        <div class="row">
                            <div class="col-md-9">
                                <h2 class="card-title">${data[i].fields.title}</h2>
                            </div>
                            <div class="col-md">
                                <div class="dropdown text-end">
                                    <a href="#" class="d-block link-dark text-decoration-none" data-bs-toggle="dropdown"
                                        aria-expanded="false" onclick="$('#id_id_post').val('${data[i].pk}')">
                                        <i class="bi bi-three-dots-vertical" alt="mdo" width="35" height="35"
                                            class="rounded-circle"></i>
                                    </a>
                                    <ul class="dropdown-menu text-small">
                                        <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                                data-bs-target="#modalTambahTask">Edit</a></li>
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                        <li><a onclick="deletePost(${data[i].pk});" class="dropdown-item" href="#">Delete</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <p class="card-text">Written by: Anonymous #${data[i].fields.creator}</p>
                        <p class="card-text">${data[i].fields.date_created}
                    </div>
                    <div class="card-body">
                        <p class="card-text">${data[i].fields.description}</p>
                        <button class="btn btn-upvote" onclick="upvote('${data[i].pk}');" id="upvote${data[i].pk}">&#128316 Upvote
                        ${data[i].fields.upvote_count}</button>
                        <a href="${url}${data[i].pk}/comment" class="btn-reply">&#128488 Reply</a>
                        <br>
                    </div>
                </div>`
                    $(`#my-post`).append(card);
                }
            }
        }
    });
}

function resetForm() {
    $('#form-edit-post').trigger("reset");
    $('#form-edit-post').removeClass('was-validated')
    $('#input-date').addClass('d-none');
    $('#modalTambahTask').modal('hide');
}

$(document).ready(function () {
    resetPost();
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