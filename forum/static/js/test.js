
function hello() {
    alert("Berhasil diklik");
}

var nameList = []
function validate_input(id) {
    var element = $(`#${id}`);
    var name_list = [];
    if (!element.checkValidity()) {
        // Hide invalid msg ke-2 (Yang nama udah ada)
    } else if (nameList.includes(element.value)) {
        // Hide invalide msg ke-1
        // Show invalid msg ke-2
        element.setCustomValidity("Invalid field.");
    } else {
        field.setCustomValidity("");
        // Show invalid msg ke-1
    }
}

$(document).ready(function() {
    $.ajax({
        url: './name',
        dataType: 'json',
        success: function(data){
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
      
            form.classList.add('was-validated')
          }, false)
        })
      })()
    var test = `<p>Test sesuatu</p>`;
    $('#placeholder').append(test);
});