# app.py
import random
from bson import ObjectId
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

@app.route('/increase_score', methods=['POST'])
def increase_score():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    result = manager.increase_flashcard_score(question)
    
    # return the new score
    flashcards = manager.db.get_all_flashcards() 
    score = 0
    for flashcard in flashcards:
        flashcard['_id'] = str(flashcard['_id'])  # Convert ObjectId to string
        if flashcard['question'] == question:
            score = str(flashcard['score'])

    return jsonify(score)

@app.route('/decrease_score', methods=['POST'])
def decrease_score():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({'error': 'Question is required'}), 400

    result = manager.decrease_flashcard_score(question)
    
    # return the new score
    flashcards = manager.db.get_all_flashcards() 
    score = 0
    for flashcard in flashcards:
        flashcard['_id'] = str(flashcard['_id'])  # Convert ObjectId to string
        if flashcard['question'] == question:
            score = str(flashcard['score'])

    return jsonify(score)

@app.route('/study_flashcards', methods=['GET'])
def study_flashcards():
    flashcards = manager.db.get_all_flashcards() 
    # Convert ObjectId to string for each flashcard
    flashcards_serialized = []
    
    for flashcard in flashcards:
        flashcard['_id'] = str(flashcard['_id'])  # Convert ObjectId to string
        flashcards_serialized.append(flashcard)

    random_flashcards = random.sample(flashcards_serialized, min(len(flashcards_serialized), len(flashcards_serialized)))  # Pick 5 random flashcards
    return jsonify(random_flashcards)

@app.route('/delete_flashcard', methods=['DELETE'])
def delete_flashcard():
    card_question = request.json.get('question')  # Get the question from the request
    manager.delete_flashcard(card_question)
    return jsonify({'message': 'Flashcard deleted successfully!'})
    


if __name__ == '__main__':
    app.run(debug=True)
