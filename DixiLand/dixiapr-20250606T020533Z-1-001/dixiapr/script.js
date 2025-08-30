const wordSets = [
  { correct: "camino", options: ["camino", "kaminno", "cammyno"] },
  { correct: "escuela", options: ["eskuela", "escuela", "escuella"] },
  { correct: "jirafa", options: ["girafa", "jirafa", "hirafa"] },
  { correct: "zapato", options: ["sapato", "zapato", "zapatho"] },
  { correct: "reloj", options: ["reloj", "reloh", "rreloj"] }
];

let currentIndex = 0;

function shuffle(array) {
  return array.sort(() => Math.random() - 0.5);
}

function loadNextWord() {
  const container = document.getElementById('word-options');
  const feedback = document.getElementById('feedback');
  feedback.textContent = '';
  feedback.style.color = '';

  if (currentIndex >= wordSets.length) {
    container.innerHTML = "<p style='font-size:24px;'>🎉 ¡Juego terminado! ¡Eres un campeón! 🏆</p>";
    document.getElementById('next-btn').style.display = "none";
    return;
  }

  const current = wordSets[currentIndex];
  const shuffled = shuffle([...current.options]);

  container.innerHTML = '';
  shuffled.forEach(word => {
    const btn = document.createElement('div');
    btn.className = 'option';
    btn.textContent = word;
    btn.onclick = () => checkAnswer(word, current.correct, btn);
    container.appendChild(btn);
  });

  currentIndex++;
}

function checkAnswer(selected, correct, element) {
  const feedback = document.getElementById('feedback');
  const options = document.querySelectorAll('.option');
  options.forEach(btn => btn.onclick = null); // desactiva más clics

  if (selected === correct) {
    feedback.innerHTML = "✅ ¡Muy bien!";
    feedback.style.color = "green";
    element.style.backgroundColor = "#b9fbc0";
  } else {
    feedback.innerHTML = "❌ ¡Ups! Esa no es.";
    feedback.style.color = "red";
    element.style.backgroundColor = "#f08080";
  }
}

window.onload = loadNextWord;
