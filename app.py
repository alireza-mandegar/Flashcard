# app.py
from flask import Flask, render_template, request, jsonify
from flashcard_manager import FlashcardManager

app = Flask(__name__)
manager = FlashcardManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    data = request.get_json()
    question = data['question']
    answer = data['answer']
    manager.add_flashcard(question, answer)     
    return jsonify({"message": "Flashcard added successfully!"})

@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    flashcards = manager.db.get_all_flashcards()
    return jsonify(flashcards)

if __name__ == '__main__':
    app.run(debug=True)
