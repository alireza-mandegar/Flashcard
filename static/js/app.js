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
      document.getElementById("add-flashcard-form").style.display = "none";
      document.getElementById("delete-flashcard-form").style.display = "none";
      displayFlashcard();
    });
}

// Function to Start adding card
function startAddingCard() {
  document.getElementById("study-container").style.display = "none";
  document.getElementById("add-flashcard-form").style.display = "block";
  document.getElementById("delete-flashcard-form").style.display = "none";
}

// Function to Start deleting card
function startDeletingCard() {
  document.getElementById("study-container").style.display = "none";
  document.getElementById("add-flashcard-form").style.display = "none";
  document.getElementById("delete-flashcard-form").style.display = "block";
}

function finishFunctions() {
  document.getElementById("study-container").style.display = "none";
  document.getElementById("add-flashcard-form").style.display = "none";
  document.getElementById("delete-flashcard-form").style.display = "none";
}

// Function to display the current flashcard
function displayFlashcard() {
  const question = flashcards[currentIndex].question;
  const answer = flashcards[currentIndex].answer;

  // Update the question and answer on the flashcard
  document.getElementById("question").innerText = question;
  document.getElementById("answer").innerText = answer;

  // Reset card to front
  const flashcardElement = document.querySelector(".flashcard");
  flashcardElement.classList.remove("flipped"); // Ensure the card starts unflipped
}

// Event listener to flip the card (reveal answer)
document.getElementById("reveal-btn").addEventListener("click", function () {
  const flashcardElement = document.querySelector(".flashcard");
  flashcardElement.classList.toggle("flipped"); // Add or remove the 'flipped' class
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

// Function to add a new flashcard
document.getElementById("add-card-btn").addEventListener("click", function () {
  const question = document.getElementById("new-question").value;
  const answer = document.getElementById("new-answer").value;

  if (!question) {
    alert("Please enter a question to add a flashcard."); // Alert user to enter a question
    return; // Exit the function if input is empty
  }

  if (!answer) {
    alert("Please enter a answer to add a flashcard."); // Alert user to enter a answer
    return; // Exit the function if input is empty
  }

  fetch("/add_flashcard", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question, answer }),
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.message);
      document.getElementById("new-question").value = ""; // Clear input
      document.getElementById("new-answer").value = ""; // Clear input
    })
    .catch((error) => console.error("Error:", error));
});

// Function to delete a flashcard
document
  .getElementById("delete-card-btn")
  .addEventListener("click", function () {
    const question = document.getElementById("delete-card-id").value;

    if (!question) {
      alert("Please enter a question to delete a flashcard."); // Alert user to enter a question
      return; // Exit the function if input is empty
    }

    fetch("/delete_flashcard", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }), // Send the question in the body
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message);
        document.getElementById("delete-card-id").value = ""; // Clear input
      })
      .catch((error) => console.error("Error:", error));
  });
