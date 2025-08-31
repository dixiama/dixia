// 🔎 BUSCADOR CON RESALTADO
document.getElementById('searchButton')?.addEventListener('click', function () {
    const input = document.getElementById('searchInput').value.trim();
    const content = document.getElementById('content');
    let text = content.textContent; // usamos solo texto para evitar errores

    if (!input) {
        content.innerHTML = text; // restaurar sin resaltado
        return;
    }

    const regex = new RegExp(`(${input})`, 'gi');
    const highlighted = text.replace(regex, '<mark>$1</mark>');
    content.innerHTML = highlighted;
});

// 🍔 MENÚ HAMBURGUESA
document.addEventListener('DOMContentLoaded', function () {
    const btn = document.getElementById('menu-btn');
    const nav = document.querySelector('header nav');

    btn.addEventListener('click', function () {
        nav.classList.toggle('show');
    });
});
