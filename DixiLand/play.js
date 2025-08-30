document.getElementById('cerrar').addEventListener('click', function() {
  document.getElementById('modal').style.display = 'none';
});

// ...existing code...

// Mostrar el modal al tocar el botón "Mapa"
document.querySelectorAll('.nav-btn')[0].addEventListener('click', function() {
  document.getElementById('mapaModal').style.display = 'flex';
});

// Cerrar el modal
document.getElementById('cerrarMapa').onclick = function() {
  document.getElementById('mapaModal').style.display = 'none';
};

// ...existing code...

// Mostrar el modal al tocar el botón "Niveles"
document.querySelectorAll('.nav-btn')[1].addEventListener('click', function() {
  document.getElementById('nivelesModal').style.display = 'flex';
});

// Cerrar el modal de niveles
document.getElementById('cerrarNiveles').onclick = function() {
  document.getElementById('nivelesModal').style.display = 'none';
};

// ...existing code...

// Mostrar el modal al tocar el botón "Perfil"
document.querySelectorAll('.nav-btn')[2].addEventListener('click', function() {
  document.getElementById('perfilModal').style.display = 'flex';
});

// Cerrar el modal de perfil
document.getElementById('cerrarPerfil').onclick = function() {
  document.getElementById('perfilModal').style.display = 'none';
};