 // JavaScript for counting words in the description field
 const descriptionField = document.querySelector('#id_description');
 const wordCountElement = document.querySelector('#word-count');
 const wordWarningElement = document.querySelector('#word-warning');

 // Function to count words
 function countWords(text) {
     const trimmedText = text.trim();
     if (trimmedText === '') {
         return 0;
     }
     return trimmedText.split(/\s+/).length;
 }

 // Initial word count on page load
 wordCountElement.textContent = `${countWords(descriptionField.value)}/150 Words`;

 // Event listener for input in description field
 descriptionField.addEventListener('input', function() {
     const words = countWords(this.value);
     wordCountElement.textContent = `${words}/150 Words`;

     // Show word count warning if exceeds 150 words
     if (words > 150) {
         wordCountElement.style.color = 'red';
         wordWarningElement.style.display = 'block';
     } else {
         wordCountElement.style.color = ''; // reset color if within limit
         wordWarningElement.style.display = 'none';
     }
 });