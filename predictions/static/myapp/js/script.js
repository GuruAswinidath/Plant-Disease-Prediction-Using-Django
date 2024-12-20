  // Library page for the search bar
  function searchDisease() {
    // Get the search input
    const searchInput = document.getElementById('searchInput').value.toLowerCase();

    // Get all disease items
    const diseaseItems = document.querySelectorAll('.disease-item');

    // Loop through all items and filter based on the title
    diseaseItems.forEach((item) => {
      const title = item.querySelector('.card-title').textContent.toLowerCase();
      if (title.includes(searchInput)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  }
