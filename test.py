from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path='coursegen_project/.env')

from coursegen_project.app.services.pdf_extractor import extract_text_from_pdf
from coursegen_project.app.services.quiz_generator import generate_quiz_from_text

def main():
    """
    Reads the course document, extracts text, generates a quiz, and prints it.
    """
    pdf_path = "Course document.pdf"

    # Check if the GROQ_API_KEY is set
    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY is not set. Please create a .env file in the 'coursegen_project' directory and add your key.")
        return

    try:
        print(f"Reading PDF file: {pdf_path}")
        with open(pdf_path, "rb") as pdf_file:
            pdf_content = pdf_file.read()

        print("Extracting text from PDF...")
        text = extract_text_from_pdf(pdf_content)

        if not text:
            print("No text could be extracted from the PDF.")
            return

        print("Generating quiz... (This might take a moment)")
        quiz = generate_quiz_from_text(text)

        if quiz:
            print("\n--- Generated Quiz ---")
            print(f"Title: {quiz.title}")
            for i, q in enumerate(quiz.questions, 1):
                print(f"\nQ{i}: {q.question_text}")
                for opt in q.options:
                    print(f"  - {opt}")
                print(f"Correct Answer: {q.correct_answer}")
                if q.explanation:
                    print(f"Explanation: {q.explanation}")
            print("\n--------------------")
        else:
            print("Failed to generate the quiz.")

    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found in the root directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()