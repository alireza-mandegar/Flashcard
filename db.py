# db.py
from pymongo import MongoClient

class Database:
    def __init__(self, db_name: str, collection_name: str):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_flashcard(self, flashcard: dict):
        """
        Inserts a new flashcard into the collection.
        """
        return self.collection.insert_one(flashcard)

    def delete_flashcard_by_question(self, question: str):
        """
        Deletes a flashcard by its question text.
        """
        return self.collection.delete_one({'question': question})

    def get_all_flashcards(self):
        """
        Retrieves all flashcards from the collection.
        """
        return list(self.collection.find())

    def search_flashcards_by_keyword(self, keyword: str):
        """
        Searches flashcards based on a keyword found in the question or answer.
        """
        return list(self.collection.find({
            '$or': [
                {'question': {'$regex': keyword, '$options': 'i'}},
                {'answer': {'$regex': keyword, '$options': 'i'}}
            ]
        }))

    def increase_score(self, question: str):
        """
        Increases the score of a flashcard by 1 based on the question.
        """
        return self.collection.update_one(
            {'question': question},
            {'$inc': {'score': 1}}
        )

    def decrease_score(self, question: str):
        """
        Decreases the score of a flashcard by 1 based on the question.
        """
        return self.collection.update_one(
            {'question': question},
            {'$inc': {'score': -1}}
        )