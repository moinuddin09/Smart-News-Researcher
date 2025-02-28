# 📰 Smart News Researcher

## Overview
Smart News Researcher is a Streamlit-based web application that fetches news articles from given URLs, extracts the content, and allows users to ask questions about the articles using Google's Gemini AI model.

### Screenshot
![Smart News Researcher](smart_news_researcher_screenshot.png)

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

## Sample News Articles
- [Tata Motors, Mahindra gain certificates for production-linked payouts](https://www.moneycontrol.com/news/business/tata-motors-mahindra-gain-certificates-for-production-linked-payouts-11281691.html)
- [Tata Motors launches Punch iCNG, price starts at Rs 7.1 lakh](https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html)
- [Buy Tata Motors; target of Rs 743: KR Choksey](https://www.moneycontrol.com/news/business/stocks/buy-tata-motors-target-of-rs-743-kr-choksey-11080811.html)

## Contributing
Feel free to submit issues or contribute via pull requests!

## License
MIT License

