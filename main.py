# main.py
import argparse
from flashcard_manager import FlashcardManager

def main():
    parser = argparse.ArgumentParser(description='Flashcard Application')
    parser.add_argument('command', choices=['add', 'delete', 'list', 'study'], help='Command to execute')
    parser.add_argument('--question', type=str, help='Flashcard question')
    parser.add_argument('--answer', type=str, help='Flashcard answer')
    args = parser.parse_args()

    manager = FlashcardManager()

    if args.command == 'add':
        manager.add_flashcard(args.question, args.answer)
    elif args.command == 'delete':
        manager.delete_flashcard(args.question)
    elif args.command == 'list':
        manager.list_flashcards()
    elif args.command == 'study':
        manager.study_flashcards()

if __name__ == '__main__':
    main()
