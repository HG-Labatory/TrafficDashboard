function loadList(jsonUrl, targetId) {
  fetch(jsonUrl)
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById(targetId);
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
    .catch(err => console.error("Fehler:", err));
}

loadList("data/news.json", "news");
loadList("data/science.json", "science");
