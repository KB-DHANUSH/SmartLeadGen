# 🧠 SmartLeadGen

**SmartLeadGen** is an AI-powered lead generation tool that combines Google's Gemini LLM and the FireCrawl API, all wrapped in a clean and interactive Streamlit interface.

---

## 🚀 Features

- 🔍 Generate business leads based on any topic or industry  
- 💬 Uses Gemini (via LangChain) to identify top businesses  
- 🌐 Enriches data with contact info (emails, phones, socials) using FireCrawl  
- 📁 Export results directly to CSV  
- 🖥️ Streamlit-powered UI — 100% Python

---

## 🛠️ Tech Stack

- Python 3.x  
- [Streamlit](https://streamlit.io)  
- [Gemini API (via LangChain)](https://ai.google.dev/gemini-api/docs)  
- [FireCrawl API](https://firecrawl.dev)  

---

## 🧪 Run Locally
 1. Clone the repo:
```bash
git clone https://github.com/KB-DHANUSH/SmartLeadGen.git
cd SmartLeadGen
```
2. Create and activate a virtual environment:
```bash
python -m venv myvenv
myvenv\Scripts\activate    
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set your API keys in .env:
```bash
Create a .env file in the root directory:

GOOGLE_API_KEY=your_gemini_key
FIRECRAWL_API_KEY=your_firecrawl_key
```
For deployment on Streamlit Cloud, use .streamlit/secrets.toml instead of .env.
---
5. Run the app 
```bash 
streamlit run streamlit_app.py
```
---
# Demo Screenshot
<img width="1920" height="900" alt="image" src="https://github.com/user-attachments/assets/8744aa4b-1c89-490c-b9cb-1473dde3f073" />
---
# Folder Structure
```bash
SmartLeadGen/
├── .streamlit/
│   └── secrets.toml          # for deployment secrets (optional)
├── firecrawler.py            # API enrichment logic
├── main.py                   # Lead generation + enrichment
├── requirements.txt
├── streamlit_app.py          # Main Streamlit app
├── .env                      # Local API keys (gitignored)
└── README.md
```
 Built by
K.B. Dhanush

⭐️ If you like the project, consider giving it a star!

