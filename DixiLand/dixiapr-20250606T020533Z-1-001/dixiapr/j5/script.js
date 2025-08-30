const questions = [
  { word: "ca_tillo", correct: "s", options: ["s", "r"] },
  { word: "ma_ana", correct: "ñ", options: ["n", "ñ"] },
  { word: "pe_cado", correct: "z", options: ["s", "z"] },
  { word: "te_lado", correct: "c", options: ["s", "c"] },
  { word: "ra_ón", correct: "t", options: ["t", "d"] }
];

let current = 0;
let score = 0;
let timeLeft = 30;
let timer;

function startGame() {
  loadQuestion();
  timer = setInterval(() => {
    timeLeft--;
    document.getElementById("timer").textContent = `⏱ ${timeLeft} seg`;
    if (timeLeft <= 0) endGame();
  }, 1000);
}

function loadQuestion() {
  const q = questions[current];
  document.getElementById("word-container").textContent = q.word;
  const optionsDiv = document.getElementById("options");
  optionsDiv.innerHTML = "";
  q.options.forEach(letter => {
    const btn = document.createElement("button");
    btn.textContent = letter;
    btn.className = "option-btn";
    btn.onclick = () => checkAnswer(letter);
    optionsDiv.appendChild(btn);
  });
}

function checkAnswer(selected) {
  const q = questions[current];
  if (selected === q.correct) score++;
  document.getElementById("score").textContent = `✔️ ${score}`;
  current++;
  if (current < questions.length) {
    loadQuestion();
  } else {
    endGame();
  }
}

function endGame() {
  clearInterval(timer);
  document.getElementById("resultModal").style.display = "flex";
  document.getElementById("finalScore").textContent =
    `Respuestas correctas: ${score} de ${questions.length}`;
  document.getElementById("nextGameBtn").onclick = () => {
    window.location.href = "/index.html"; // o el juego siguiente
  };
}

startGame();
