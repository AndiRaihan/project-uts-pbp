var url = window.location.href

function resetComment() {
    $.ajax({
        url: `${url}json/`,
        datatype: `json`,
        success: function (data) {
            for (var i = 0; i < data.length; i++) {
                var comment = `<div class="card col-lg-4 col-md-6 col-sm-12" style="width: 15rem;">
            <div class="card-body">
                <h4 class="card-text">Anonymous #${data[i].fields.user}</h4>
                <p class="card-text">${data[i].fields.date_created}</p>
                <p class="card-text">${data[i].fields.comment}</p>
            </div>
        </div>`;
                $(`#container-comment`).append(comment);
            }
        },
    });
}

function addComment() {
    $.ajax({
        type: 'POST',
        url: `${url}add/`,
        data: {
            comment: $(`#comment-text`).val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(data) {
            if (data.msg === 'success') {
                var comment = `<div class="card col-lg-4 col-md-6 col-sm-12" style="width: 15rem;">
            <div class="card-body">
                <h4 class="card-text">Anonymous #${data.comment[0].fields.user}</h4>
                <p class="card-text">${data.comment[0].fields.date_created}</p>
                <p class="card-text">${data.comment[0].fields.comment}</p>
            </div>
        </div>`;
                $(`#container-comment`).append(comment);
                $(`#form-comment`).trigger("reset");
            }
        }

    });
}

$(document).ready(function () {
    resetComment();
});