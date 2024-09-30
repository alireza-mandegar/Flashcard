// static/js/app.js
document
  .getElementById("flashcard-form")
  .addEventListener("submit", function (e) {
    e.preventDefault();
    const question = document.getElementById("question").value;
    const answer = document.getElementById("answer").value;

    fetch("/add_flashcard", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question: question, answer: answer }),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message);
        fetchFlashcards(); // Refresh the flashcard list
      });
  });

function fetchFlashcards() {
  fetch("/flashcards")
    .then((response) => response.json())
    .then((data) => {
      const container = document.getElementById("flashcard-container");
      container.innerHTML = ""; // Clear previous results
      data.forEach((flashcard) => {
        const div = document.createElement("div");
        div.innerHTML = `<strong>Q:</strong> ${flashcard.question} <br> <strong>A:</strong> ${flashcard.answer}`;
        container.appendChild(div);
      });
    });
}
