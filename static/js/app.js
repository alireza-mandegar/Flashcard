// static/js/app.js

let flashcards = [];
let currentIndex = 0;

// Function to start study session
function startStudy() {
  fetch("/study_flashcards")
    .then((response) => response.json())
    .then((data) => {
      flashcards = data;
      currentIndex = 0;
      document.getElementById("study-container").style.display = "block";
      displayFlashcard();
    });
}

// Function to display the current flashcard
function displayFlashcard() {
  if (flashcards.length === 0) {
    alert("No flashcards available for study.");
    return;
  }

  const flashcard = flashcards[currentIndex];
  document.getElementById("question").innerText = flashcard.question;
  document.getElementById("answer").innerText = flashcard.answer;
  document.getElementById("answer").style.display = "none"; // Hide answer initially
}

// Event listener to reveal the answer
document.getElementById("reveal-btn").addEventListener("click", function () {
  document.getElementById("answer").style.display = "block"; // Show answer
});

// Event listener for the "Next" button
document.getElementById("next-btn").addEventListener("click", function () {
  if (currentIndex < flashcards.length - 1) {
    currentIndex++;
    displayFlashcard();
  } else {
    alert("You've reached the end of the flashcards!");
  }
});

// Event listener for the "Previous" button
document.getElementById("prev-btn").addEventListener("click", function () {
  if (currentIndex > 0) {
    currentIndex--;
    displayFlashcard();
  } else {
    alert("You're at the first flashcard!");
  }
});
