function upvote(id) {
    $.ajax({
        url: `./${id}/upvote`,
        datatype: 'json',
        success: function(data){
            $(`#upvote${id}`).html(`&#128316 Upvote ${data.upvote}`);
        }
    });
}