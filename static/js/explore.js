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

    $('.card__wishlist').on('click', function() {
        var button = $(this);
        var artworkId = button.data('artwork-id');
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

//validate form
  function validateForm() {
    var medium = document.getElementById('query').value;
    var medium = document.getElementById('medium').value;
    var genre = document.getElementById('genre').value;
    var style = document.getElementById('style').value;
    var priceMin = document.getElementById('price_range_min').value;
    var priceMax = document.getElementById('price_range_max').value;

    // Check if at least one filter is selected or filled
    if (query||medium || genre || style || priceMin || priceMax) {
        return true; // Allow form submission
    } else {
        alert('Please choose at least one filter option.');
        return false; // Prevent form submission
    }
}

