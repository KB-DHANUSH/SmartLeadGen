import json
import streamlit as st
from firecrawler import scrape_website
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# ✅ Get API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# 🔹 Set up Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.6
)

parser = StrOutputParser()

# 🔹 Prompt to generate leads
lead_gen_prompt = PromptTemplate.from_template("""
You are a smart business analyst. Generate a list of 5 businesses based on the user's interest below.

Respond only with a JSON list of objects. Each object must include:
- name
- website (if known or guessable)
- category
- location (if applicable)

Interest: {interest}
""")

# 🔹 Function to generate leads
def generate_leads(interest: str):
    chain = lead_gen_prompt | llm | parser
    response = chain.invoke({"interest": interest})

    try:
        if response.strip().startswith("```"):
            response = response.strip().lstrip("```json").strip("`").strip()
        leads = json.loads(response)
    except Exception as e:
        print("Parsing failed:", e)
        print("Raw response was:\n", response)
        leads = []

    return leads

# 🔹 Enrich each lead with FireCrawl
def enrich_leads(leads):
    enriched = []
    for lead in leads:
        website = lead.get("website")
        if website:
            extra = scrape_website(website)
            if "error" in extra:
                lead["Enrichment Error"] = extra["error"]
            else:
                lead.update(extra)
        else:
            lead["Enrichment Error"] = "No website to scrape"
        enriched.append(lead)
    return enriched

# 🔹 Main function to run everything
def get_enriched_leads(interest: str):
    print(f"[+] Generating leads for: {interest}")
    leads = generate_leads(interest)
    enriched = enrich_leads(leads)
    return enriched
