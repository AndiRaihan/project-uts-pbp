function showMyProfile(data) {
    document.getElementById('aliasView').value = data[0].fields.alias
    document.getElementById('profpic').src = "/images/" + data[0].fields.image
}

function editProfile(e) {
    e.preventDefault()
    var form = new FormData(document.getElementById("editForm"))

    $.ajax({
        url: "edit",
        type: "POST",
        data: form,
        success: function () {
            $.get("/myprofile/json", showMyProfile)
        },
        error: function (response) {console.log(response)},
        cache: false,
        contentType: false,
        processData: false,
    });
}

$(document).ready(function () {
    $.get("/myprofile/json", showMyProfile);
    $("#save").click(editProfile);
})