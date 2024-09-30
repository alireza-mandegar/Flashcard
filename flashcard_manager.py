# flashcard_manager.py
from db import Database
from flashcard import Flashcard
import random

class FlashcardManager:
    def __init__(self):
        # Connect to MongoDB using the Database layer
        self.db = Database('flashcards_db', 'flashcards')

    def add_flashcard(self, question: str, answer: str, tags: list = None):
        """
        Adds a new flashcard to the database.
        """
        flashcard = Flashcard(question=question, answer=answer, tags=tags)
        result = self.db.insert_flashcard(flashcard.to_dict())
        print(f"Flashcard added with id: {result.inserted_id}")

    def delete_flashcard(self, question: str):
        """
        Deletes a flashcard by matching the question.
        """
        result = self.db.delete_flashcard_by_question(question)
        if result.deleted_count > 0:
            print(f"Flashcard deleted successfully.")
        else:
            print("Flashcard not found.")

    def list_flashcards(self):
        """
        Lists all flashcards from the database.
        """
        flashcards = self.db.get_all_flashcards()
        for flashcard in flashcards:
            print(f"Question: {flashcard['question']}, Answer: {flashcard['answer']}")

    def study_flashcards(self, num_cards: int = 5):
        """
        Retrieves a set of random flashcards for studying.
        """
        flashcards = self.db.get_all_flashcards()
        study_cards = random.sample(flashcards, min(len(flashcards), num_cards))
        for flashcard in study_cards:
            print(f"Question: {flashcard['question']}")
            input("Press Enter to show the answer...")
            print(f"Answer: {flashcard['answer']}\n")

    def search_flashcards(self, keyword: str):
        """
        Searches for flashcards that match the keyword in question or answer.
        """
        flashcards = self.db.search_flashcards_by_keyword(keyword)
        if flashcards:
            for flashcard in flashcards:
                print(f"Question: {flashcard['question']}, Answer: {flashcard['answer']}")
        else:
            print("No matching flashcards found.")
