import os
import json
from dotenv import load_dotenv
from firecrawler import scrape_website
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.6
)

parser = StrOutputParser()

lead_gen_prompt = PromptTemplate.from_template("""
You are a smart business analyst. Generate a list of 5 businesses based on the user's interest below.

Respond only with a JSON list of objects. Each object must include:
- name
- website (if known or guessable)
- category
- location (if applicable)

Interest: {interest}
""")

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

def get_enriched_leads(interest: str):
    print(f"[+] Generating leads for: {interest}")
    leads = generate_leads(interest)
    enriched = enrich_leads(leads)
    return enriched
