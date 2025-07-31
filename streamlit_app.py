import streamlit as st
from main import get_enriched_leads
import pandas as pd

st.set_page_config(page_title="SmartLeadGen", layout="wide")
st.title("SmartLeadGen: AI-Powered Lead Generator")
st.markdown("Enter a topic or industry and get a list of enriched business leads.")

interest = st.text_input("What kind of leads are you looking for?", placeholder="e.g. Top AI startups in India")

if st.button("Generate Leads") and interest:
    with st.spinner("Generating and enriching leads..."):
        leads = get_enriched_leads(interest)

        if leads:
            df = pd.DataFrame(leads)
            df = df.replace(to_replace={}, value="No data found")

            st.subheader("🔍 Enriched Leads")
            st.dataframe(df)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download CSV", data=csv, file_name="leads.csv", mime="text/csv")

            if "Enrichment Error" in df.columns:
                errors = df[df["Enrichment Error"].notna()]
                if not errors.empty:
                    st.warning("⚠️ Some leads failed to enrich:")
                    st.dataframe(errors)
        else:
            st.error("No leads found or failed to parse the output.")
