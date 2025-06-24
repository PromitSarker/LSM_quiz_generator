<<<<<<< HEAD
# LSM_quiz_generator
=======
# LSM Quiz Generator

This project is a quiz generation application that uses a Large Language Model (LLM) to create quizzes from from text. It is built using FastAPI.

## Project Structure

- `app/`: Contains the main application code.
  - `main.py`: The entry point of the FastAPI application.
  - `api/`: Contains the API endpoints and routing.
  - `core/`: Contains the core logic like configuration.
  - `schemas/`: Contains the Pydantic schemas for data validation.
  - `services/`: Contains the business logic for PDF extraction and quiz generation.
- `requirements.txt`: The list of Python dependencies.
- `.env`: The file to store environment variables (you need to create this).

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd coursegen_project
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create the `.env` file:**
    Create a file named `.env` in the `coursegen_project` directory and add your Groq API key to it:
    ```
    GROQ_API_KEY="your_actual_groq_api_key"
    OPENAI_API_KEY="your_openai_api_key_if_needed"
    ```
    **Note:** The application is now configured to use Groq for the Llama 3 model. You can get a Groq API key from their website.

## How to Run the Application

1.  **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```

2.  **Access the API documentation:**
    Open your browser and go to `http://127.0.0.1:8000/docs`. You will see the Swagger UI documentation for the API.

3.  **Use the API:**
    You can use the `/api/v1/generate-quiz/` endpoint to upload a PDF file and get a quiz in return.

# Byte-compiled / optimized / DLL


>>>>>>> 2939c0d (Initial commit)
