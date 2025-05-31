import streamlit as st
def resources_page():
    st.header("📚 Resource Center")

    resources = {
        "Social Security": "https://www.ssa.gov/",
        "Medicare": "https://www.medicare.gov/",
        "Consumer Financial Protection Bureau - Senior Resources": "https://www.consumerfinance.gov/consumer-tools/seniors/",
        "AARP Fraud Watch Network": "https://www.aarp.org/money/scams-fraud/",
        "National Council on Aging": "https://www.ncoa.org/"
    }

    for name, url in resources.items():
        st.markdown(f"[{name}]({url})")
