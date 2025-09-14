// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Selecciona el botón de menú y el elemento de navegación
    const menuBtn = document.getElementById('menu-btn');
    const navMenu = document.querySelector('header nav');

    // Añade un "escuchador de eventos" para el clic en el botón
    menuBtn.addEventListener('click', function() {
        // Alterna (añade/quita) la clase 'show' en el menú de navegación
        navMenu.classList.toggle('show');
    });
});