# 🧠 SmartLeadGen

**SmartLeadGen** is an AI-powered lead generation tool built with Gemini LLM and FireCrawl, wrapped in a clean Streamlit interface.

---

## 🚀 Features
- Generate business leads using user-defined interests
- Use Gemini API to generate leads based on a topic
- Enrich leads with contact info using FireCrawl
- Export results as a CSV
- 100% Python + Streamlit

---

## 🛠️ Tech Stack
- Python
- Streamlit
- LangChain + Gemini API
- FireCrawl API

---

## 🧪 How to Run Locally

1. **Clone the repo:**
```bash
git clone https://github.com/KB-DHANUSH/SmartLeadGen.git
cd SmartLeadGen
```
2. Create a virtual environment:
```bash
python -m venv myvenv
source myvenv/Scripts/activate  # On Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Add your API keys to .env:
```bash
GOOGLE_API_KEY=your_gemini_key
FIRECRAWL_API_KEY=your_firecrawl_key
```
5. Run the app:
```bash
streamlit run app.py
```
# Demo Screenshot
<img width="1920" height="900" alt="image" src="https://github.com/user-attachments/assets/8744aa4b-1c89-490c-b9cb-1473dde3f073" />

---
#  Folder Structure
```bash
SmartLeadGen/
├── app.py
├── main.py
├── firecrawler.py
├── .env
├── requirements.txt
└── README.md
```
#  Built by
https://github.com/KB-DHANUSH

