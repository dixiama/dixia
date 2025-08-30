const sentences = [
  { text: "El gato juega con una pelota.", makesSense: true },
  { text: "El sol desayuna zapatos.", makesSense: false },
  { text: "María lee un libro en el parque.", makesSense: true },
  { text: "El avión nada en la sopa.", makesSense: false },
  { text: "Los niños ríen en el recreo.", makesSense: true }
];

let currentSentence = 0;
let totalAciertos = 0;
let tiempo = 30;
let timer;

const aciertosEl = document.querySelector('.aciertos');
const tiempoEl = document.querySelector('.tiempo');
const modal = document.getElementById('resultadoModal');
const resultadoTexto = document.getElementById('resultadoTexto');
const botonSiguienteJuego = document.getElementById('next-game-btn');

function iniciarJuego() {
  totalAciertos = 0;
  currentSentence = 0;
  tiempo = 30;
  aciertosEl.textContent = `✔ ${totalAciertos}`;
  tiempoEl.textContent = `⏱ ${tiempo} seg`;
  mostrarFrase();

  clearInterval(timer);
  timer = setInterval(() => {
    tiempo--;
    tiempoEl.textContent = `⏱ ${tiempo} seg`;
    if (tiempo <= 0) {
      clearInterval(timer);
      mostrarResultado();
    }
  }, 1000);
}

function mostrarFrase() {
  const s = sentences[currentSentence];
  document.getElementById("sentence").textContent = s.text;
  document.getElementById("feedback").textContent = "";
  document.querySelectorAll(".options button").forEach(btn => btn.disabled = false);
}

function checkAnswer(answer) {
  const correcto = sentences[currentSentence].makesSense;
  const feedback = document.getElementById("feedback");

  if (answer === correcto) {
    feedback.textContent = "🎉 ¡Muy bien!";
    feedback.style.color = "green";
    totalAciertos++;
    aciertosEl.textContent = `✔ ${totalAciertos}`;
  } else {
    feedback.textContent = "❌ Ups, intenta de nuevo.";
    feedback.style.color = "red";
  }

  document.querySelectorAll(".options button").forEach(btn => btn.disabled = true);
}

function nextSentence() {
  currentSentence++;
  if (currentSentence >= sentences.length) {
    clearInterval(timer);
    mostrarResultado();
  } else {
    mostrarFrase();
  }
}

function mostrarResultado() {
  resultadoTexto.textContent = `Respondiste correctamente ${totalAciertos} de ${sentences.length} frases.`;
  botonSiguienteJuego.onclick = () => {
    window.location.href = "../j3/index.html";
  };
  modal.style.display = 'flex';
}

window.onload = iniciarJuego;
