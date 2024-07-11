
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

