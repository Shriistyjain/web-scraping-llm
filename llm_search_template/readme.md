# **LLM-based RAG Search System**

## **Overview**

This project is a **Retrieval-Augmented Generation (RAG)** system that retrieves content from the internet, processes it, and uses a **Large Language Model (LLM)** to generate responses. It consists of:

- **Backend**: A Flask API that retrieves web content, processes it, and generates responses using GPT-4.
- **Front End**: A Streamlit app for user interaction.

---

## **Features**

- Fetches relevant web pages using the Serper API.
- Processes content to extract meaningful text.
- Generates responses using OpenAI's GPT-4.
- Provides an interactive interface for queries.

---

## **Technologies Used**

- **Backend**: Flask, Requests, BeautifulSoup, OpenAI API
- **Front End**: Streamlit
- **Utilities**: dotenv for managing API keys.

---

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd project-folder
2. Set Up Environment
Create and activate a virtual environment:

bash
Copy code
# On Linux/Mac
python -m venv env
source env/bin/activate

# On Windows
python -m venv env
env\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
3. Add API Keys
Create a .env file in the root directory and add the following:

SERPER_API_KEY=<your-serper-api-key>
OPENAI_API_KEY=<your-openai-api-key>
4. Run the Applications
Backend: Start the Flask app:


python app.py
The backend will be available at http://localhost:5001.

Front End: Start the Streamlit app:

streamlit run frontend_app.py
The front end will be available at http://localhost:8501.