$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    $('.card__wishlist').on('click', function(e) {
        e.preventDefault();
        var button = $(this);
        var url = button.data('url');
        $.ajax({
            url: url,
            method: "POST",
            headers: { 'X-CSRFToken': csrftoken },
            success: function(data) {
                if (data.added) {
                    button.text('Added to Favourites');
                } else {
                    button.text('Add to Favourites');
                }
            }
        });
    });
});