function loadList(jsonUrl, targetId) {
  fetch(jsonUrl)
    .then(response => response.json())
    .then(data => {
      const list = document.getElementById(targetId);
      list.innerHTML = "";

      data.items.forEach(item => {
        const li = document.createElement("li");
        li.innerHTML = `
          <a href="${item.url}" target="_blank">
            ${item.title}
          </a>
        `;
        list.appendChild(li);
      });
    })
    .catch(err => {
      console.error("Fehler beim Laden:", jsonUrl, err);
    });
}

// Verkehrsmeldungen
loadList("data/news.json", "news");

// Verkehrswissenschaft
loadList("data/science.json", "science");
