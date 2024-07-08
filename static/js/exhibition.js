

//add exhibition.js

function triggerFileInput() {
    document.getElementById('fileInput').click();
}

$(document).ready(function() {
    $('#fileInput').change(function() {
        previewImage(this);
    });
});

function previewImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            $('#preview').attr('src', e.target.result).show();
        };

        reader.readAsDataURL(input.files[0]);
        $('.file-name').text(input.files[0].name);
    } else {
        $('#preview').hide();
        $('.file-name').text('No file chosen');
    }
}
