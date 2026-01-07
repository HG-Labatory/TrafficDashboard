function loadList(jsonUrl, targetId) {
  fetch(jsonUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error("HTTP-Fehler " + response.status);
      }
      return response.json();
    })
    .then(data => {
      const list = document.getElementById(targetId);
      if (!list) return;

      list.innerHTML = "";

      data.items.forEach(item => {
        const li = document.createElement("li");

        li.innerHTML = `
          <a href="${item.url}" target="_blank" rel="noopener">
            ${item.title}
          </a>
          ${item.summary ? `<div class="summary">${item.summary}</div>` : ""}
        `;

        list.appendChild(li);
      });
    })
    .catch(err => {
      console.error("Fehler beim Laden:", jsonUrl, err);
    });
}

// Daten laden
loadList("data/news.json", "news");
loadList("data/science.json", "science");
