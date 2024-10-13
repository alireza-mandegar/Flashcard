# flashcard.py
class Flashcard:
    def __init__(self, question: str, answer: str, score: int = 0):
        self.question = question
        self.answer = answer
        self.score = score

    def to_dict(self):
        """
        Converts the Flashcard object into a dictionary for MongoDB storage.
        """
        return {
            'question': self.question,
            'answer': self.answer,
            'score': self.score
        }