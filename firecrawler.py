import requests
import streamlit as st

# ✅ Get API key from Streamlit secrets
FIRECRAWL_API_KEY = st.secrets["FIRECRAWL_API_KEY"]

def scrape_website(url):
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "url": url
    }

    response = requests.post("https://api.firecrawl.dev/v1/scrape", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return {
            "title": result.get("meta", {}).get("title"),
            "description": result.get("meta", {}).get("description"),
            "emails": result.get("emails", []),
            "phones": result.get("phones", []),
            "socials": result.get("socials", {}),
            "address": result.get("address", {})
        }
    else:
        return {"error": f"FireCrawl error: {response.status_code} - {response.text}"}
