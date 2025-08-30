const rondas = [
  [["mere", "mero", "pero", "muro", "mego"], ["mere", "pero", "mego", "mero", "muro"]],
  [["lupa", "palo", "puma", "lomo", "tiza"], ["lomo", "tiza", "puma", "palo", "lupa"]],
  [["casa", "saco", "pico", "pisa", "sopa"], ["pico", "pisa", "sopa", "saco", "casa"]]
];

let rondaActual = 0;
let seleccion1 = null;
let seleccion2 = null;
let aciertos = 0;
let totalAciertos = 0;
let tiempo = 30;
let timer;

const col1 = document.getElementById('col1');
const col2 = document.getElementById('col2');
const aciertosEl = document.querySelector('.aciertos');
const tiempoEl = document.querySelector('.tiempo');
const modal = document.getElementById('resultadoModal');
const resultadoTexto = document.getElementById('resultadoTexto');
const botonSiguienteJuego = document.getElementById('next-game-btn'); // <- agregado

function iniciarRonda() {
  seleccion1 = null;
  seleccion2 = null;
  aciertos = 0;
  aciertosEl.textContent = `✔ ${totalAciertos}`;
  tiempo = 30;
  tiempoEl.textContent = `⏱ ${tiempo} seg`;

  col1.innerHTML = "";
  col2.innerHTML = "";

  const [izquierda, derecha] = rondas[rondaActual];

  izquierda.forEach(p => col1.appendChild(crearPalabra(p, 1)));
  derecha.forEach(p => col2.appendChild(crearPalabra(p, 2)));

  clearInterval(timer);
  timer = setInterval(() => {
    tiempo--;
    tiempoEl.textContent = `⏱ ${tiempo} seg`;
    if (tiempo === 0) {
      clearInterval(timer);
      pasarSiguienteRonda();
    }
  }, 1000);
}

function crearPalabra(palabra, columna) {
  const div = document.createElement('div');
  div.className = 'word';
  div.textContent = palabra;
  div.dataset.valor = palabra;

  div.addEventListener('click', () => {
    if (div.classList.contains('matched')) return;

    if (columna === 1) {
      if (seleccion1) seleccion1.classList.remove('selected');
      seleccion1 = div;
      div.classList.add('selected');
    } else {
      if (seleccion2) seleccion2.classList.remove('selected');
      seleccion2 = div;
      div.classList.add('selected');
    }

    if (seleccion1 && seleccion2) {
      if (seleccion1.dataset.valor === seleccion2.dataset.valor) {
        seleccion1.classList.add('matched');
        seleccion2.classList.add('matched');
        totalAciertos++;
        aciertos++;
        aciertosEl.textContent = `✔ ${totalAciertos}`;
      }
      setTimeout(() => {
        if (seleccion1) seleccion1.classList.remove('selected');
        if (seleccion2) seleccion2.classList.remove('selected');
        seleccion1 = null;
        seleccion2 = null;
        if (aciertos === 5) {
          clearInterval(timer);
          pasarSiguienteRonda();
        }
      }, 300);
    }
  });

  return div;
}

function pasarSiguienteRonda() {
  rondaActual++;
  if (rondaActual < rondas.length) {
    iniciarRonda();
  } else {
    mostrarResultado();
  }
}

function mostrarResultado() {
  resultadoTexto.textContent = `Has encontrado ${totalAciertos} coincidencias correctas.`;
  botonSiguienteJuego.textContent = "Pasar al siguiente juego";
  botonSiguienteJuego.onclick = () => {
    window.location.href = "../j5/index.html";
  };
  modal.style.display = 'flex';
}

window.onload = iniciarRonda;
