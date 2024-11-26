from flask import Flask, request, jsonify
import os
from utils import search_articles, fetch_article_content, concatenate_content, generate_answer

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    """
    Handles the POST request to '/query'. Processes the query and returns a response.
    """
    data = request.get_json()
    query = data.get("query", "")

    if not query:
        return jsonify({"error": "No query provided."}), 400

    try:
        # Step 1: Search and scrape articles based on the query
        articles = search_articles(query)
        
        # Step 2: Concatenate content from the scraped articles
        content = concatenate_content(articles)

        # Step 3: Generate an answer using the LLM
        answer = generate_answer(content, query)

        # Return the answer as JSON
        return jsonify({"answer": answer}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
