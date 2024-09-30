# flashcard.py
class Flashcard:
    def __init__(self, question: str, answer: str, tags: list = None):
        self.question = question
        self.answer = answer
        self.tags = tags or []

    def to_dict(self):
        """
        Converts the Flashcard object into a dictionary for MongoDB storage.
        """
        return {
            'question': self.question,
            'answer': self.answer,
            'tags': self.tags
        }
