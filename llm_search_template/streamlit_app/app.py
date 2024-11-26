import streamlit as st
import requests

st.title("LLM-based RAG Search")

# Input for user query
query = st.text_input("Enter your query:")

if st.button("Search"):
    try:
        # Make a POST request to the Flask API
        url = "http://localhost:5001/query"
        response = requests.post(url, json={"query": query})

        if response.status_code == 200:
            # Display the generated answer
            answer = response.json().get("answer", "No answer received.")
            st.write("Answer:", answer)
        else:
            st.error(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
