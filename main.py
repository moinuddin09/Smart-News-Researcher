import os
import streamlit as st
from newspaper import Article
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key securely
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("Gemini API key is missing. Set it in a .env file.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

# Streamlit UI
st.title("📰 Smart News Researcher")
st.sidebar.title("🔗 Enter News URLs")

# User input
urls = [st.sidebar.text_input(f"URL {i+1}", key=f"url{i}") for i in range(3)]

# Function to fetch articles
def fetch_articles():
    articles = []
    for url in urls:
        if url.strip():
            try:
                article = Article(url)
                article.download()
                article.parse()
                articles.append({"title": article.title, "text": article.text, "source": url})
            except Exception as e:
                st.error(f"Error processing {url}: {str(e)}")
    return articles

# Store articles in session state
if "articles" not in st.session_state:
    st.session_state.articles = []

if st.sidebar.button("Fetch & Analyze"):
    st.session_state.articles = fetch_articles()
    st.success("✅ Articles fetched successfully!")

# Display extracted articles
if st.session_state.articles:
    for idx, article in enumerate(st.session_state.articles):
        with st.expander(f"📝 {article['title']}"):
            st.write(article['text'][:1000] + "...")
            st.write(f"🔗 [Source]({article['source']})")

# User Query Section
query = st.text_area("🔍 Ask a question about the articles:", key="query")

# Function to process query
def process_query():
    if query and st.session_state.articles:
        combined_text = "\n\n".join([f"Title: {a['title']}\n{a['text']}" for a in st.session_state.articles])
        prompt = (
            f"You are an expert news analyst. Analyze the following news articles and answer the user's question concisely.\n\n"
            f"{combined_text}\n\nQuestion: {query}\nAnswer (also provide the relevant source from which the answer is derived):"
        )

        with st.spinner("Analyzing and generating response..."):
            model = genai.GenerativeModel("gemini-1.5-pro")  # Valid Gemini model
            response = model.generate_content(prompt)

        st.header("📢 Answer")
        st.markdown(f"<div style='font-size:18px; font-weight:bold;'>{response.text}</div>", unsafe_allow_html=True)

        # Extract relevant source from response
        relevant_source = None
        for article in st.session_state.articles:
            if article['title'] in response.text or article['text'][:100] in response.text:
                relevant_source = article['source']
                break

        # Display the relevant source
        if relevant_source:
            st.subheader("🔗 Source")
            st.write(f"[Relevant Source]({relevant_source})")
        else:
            st.warning("⚠️ No specific source identified.")

        # Summarized Key Points
        st.subheader("📌 Key Points")
        summary_prompt = f"Summarize the key points from the following answer:\n\n{response.text}"
        summary_response = model.generate_content(summary_prompt)
        st.write(summary_response.text)

# Auto-process query when Ctrl+Enter is pressed
if query and st.session_state.articles:
    process_query()