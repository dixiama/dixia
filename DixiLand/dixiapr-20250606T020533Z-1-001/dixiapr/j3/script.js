const rounds = [
  ["casa", "sol", "pan"],
  ["flor", "lápiz", "zapato", "mar"],
  ["gato", "libro", "manzana", "pelota", "árbol"]
];

let currentRound = 0;
let userSequence = [];

function startGame() {
  userSequence = [];
  const sequenceDiv = document.getElementById("word-sequence");
  const wordButtons = document.getElementById("word-buttons");
  const words = rounds[currentRound];

  document.getElementById("feedback").textContent = "";
  document.getElementById("start-btn").style.display = "none";
  document.getElementById("next-btn").style.display = "none";

  sequenceDiv.textContent = words.join(" - ");
  wordButtons.innerHTML = "";

  setTimeout(() => {
    sequenceDiv.textContent = "🔁 Ahora repite el orden:";
    renderWordButtons(words);
  }, 3000 + words.length * 400);
}

function renderWordButtons(words) {
  const wordButtons = document.getElementById("word-buttons");
  wordButtons.innerHTML = "";
  const shuffled = [...words].sort(() => Math.random() - 0.5);

  shuffled.forEach(word => {
    const btn = document.createElement("button");
    btn.textContent = word;
    btn.onclick = () => handleWordClick(word);
    wordButtons.appendChild(btn);
  });
}

function handleWordClick(word) {
  userSequence.push(word);
  if (userSequence.length === rounds[currentRound].length) {
    validateSequence();
  }
}

function validateSequence() {
  const correct = rounds[currentRound];
  const feedback = document.getElementById("feedback");

  if (arraysEqual(correct, userSequence)) {
    feedback.textContent = "🎉 ¡Muy bien! Memoria poderosa.";
    feedback.style.color = "green";
    localStorage.setItem(`juego_memoria_verbal_r${currentRound + 1}`, "correcto");
  } else {
    feedback.textContent = "❌ Oh no... el orden no es correcto.";
    feedback.style.color = "red";
    localStorage.setItem(`juego_memoria_verbal_r${currentRound + 1}`, "incorrecto");
  }

  document.getElementById("next-btn").style.display = "inline-block";
  document.getElementById("word-buttons").innerHTML = "";
}

function nextRound() {
  currentRound++;
  const sequenceDiv = document.getElementById("word-sequence");

  if (currentRound >= rounds.length) {
    sequenceDiv.innerHTML = "";

    const mensaje = document.createElement("p");
    mensaje.textContent = "🏁 ¡Terminaste todas las rondas!";
    sequenceDiv.appendChild(mensaje);

    const boton = document.createElement("button");
    boton.innerHTML = "Pasar al siguiente juego";
    boton.onclick = () => {
      window.location.href = "../j4/index.html";
    };
    boton.style.marginTop = "20px";
    sequenceDiv.appendChild(boton);

    document.getElementById("feedback").textContent = "";
    document.getElementById("start-btn").style.display = "none";
    document.getElementById("next-btn").style.display = "none";
  } else {
    document.getElementById("start-btn").style.display = "inline-block";
    document.getElementById("feedback").textContent = "";
    sequenceDiv.textContent = "";
  }
}

function arraysEqual(a, b) {
  return a.length === b.length && a.every((v, i) => v === b[i]);
}
