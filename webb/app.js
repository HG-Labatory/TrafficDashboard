fetch("../data/news.json")
  .then(r => r.json())
  .then(data => {
    const list = document.getElementById("news");

    data.items.forEach(item => {
      const li = document.createElement("li");
      li.innerHTML = `
        <a href="${item.url}" target="_blank">
          ${item.title}
        </a>
        <small>(${item.source})</small>
      `;
      list.appendChild(li);
    });
  });
