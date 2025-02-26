# 📰 Smart News Researcher

## Overview
Smart News Researcher is a Streamlit-based web application that fetches news articles from given URLs, extracts the content, and allows users to ask questions about the articles using Google's Gemini AI model.

## Features
- Fetch news articles from URLs
- Display extracted content
- AI-powered question-answering
- Summarized key points

## Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/moinuddin09/smart-news-researcher.git
cd smart-news-researcher
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
- Create a `.env` file in the project root.
- Add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run the Application
```bash
streamlit run app.py
```

## Usage
1. Enter news article URLs in the sidebar.
2. Click "Fetch & Analyze" to extract content.
3. Ask questions about the articles in the text area.
4. View AI-generated answers along with key points and sources.

## Contributing
Feel free to submit issues or contribute via pull requests!

## License
MIT License
