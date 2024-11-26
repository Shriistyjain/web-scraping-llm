import os
import requests
from bs4 import BeautifulSoup
import openai

# Load API keys from environment variables
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def search_articles(query):
    """
    Searches for articles related to the query using Serper API.
    Returns a list of dictionaries containing article URLs, headings, and text.
    """
    headers = {"X-API-KEY": SERPER_API_KEY}
    params = {"q": query}
    response = requests.get("https://api.serper.dev/search", headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json().get("organic", [])
    articles = [{"url": res["url"], "title": res["title"]} for res in search_results[:5]]
    return articles

def fetch_article_content(url):
    """
    Fetches the article content, extracting headings and text.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all(['p', 'h1', 'h2'])
    content = "\n".join([p.get_text() for p in paragraphs])
    return content.strip()

def concatenate_content(articles):
    """
    Concatenates the content of the provided articles into a single string.
    """
    full_text = ""
    for article in articles:
        content = fetch_article_content(article["url"])
        full_text += f"Title: {article['title']}\n{content}\n\n"
    return full_text

def generate_answer(content, query):
    """
    Generates an answer from the concatenated content using GPT-4.
    """
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": f"Query: {query}\nContent: {content}"}
        ]
    )
    return response.choices[0].message.content
