# app.py

import streamlit as st
from chat_page import chat_page
from visualizations import render_visualization_tab
from alert_reminders import alerts_reminders
from investment_simulator import investment_simulator
from resources import resources_page

st.set_page_config(page_title="Finance Buddy", layout="wide")

st.title("💰 Finance Buddy")
st.write("Helping you understand money, the economy, and more — simply and clearly.")

# Tabs for chatbot and visualizations
tab1, tab2, tab3, tab4, tab5= st.tabs(["🧠 Ask the Chatbot", "📊 Visual Insights", "alerts", "safe investment simulator", "resources"])

with tab1:
    chat_page()

with tab2:
    st.subheader("📈 U.S. Inflation Trends Over Time")
    render_visualization_tab()  # we'll define this `run()` function in visualization.py


with tab3:
    alerts_reminders()

with tab4:
    investment_simulator()

with tab5:
    resources_page()
