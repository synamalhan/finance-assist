# app.py

import streamlit as st
from chat_page import chat_page
from visualizations import render_visualization_tab
from alert_reminders import alerts_reminders
from investment_simulator import investment_simulator
from resources import resources_page

# Set page configuration
st.set_page_config(page_title="Finance Buddy", layout="wide")

# App title and welcome message
st.title("💰 Finance Buddy")
st.write(
    "Welcome to **Finance Buddy**, your simple and friendly guide to understanding money, "
    "the economy, and smart investing. Whether you're retired, planning, or just curious — "
    "we're here to help, every step of the way. 💡"
)

# Tabs for each section
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧠 Ask the Chatbot",
    "📊 Visual Insights",
    "🔔 Alerts & Reminders",
    "💼 Safe Investment Simulator",
    "📚 Helpful Resources"
])

# 🧠 Tab 1 – Chatbot
with tab1:
    st.header("🧠 Ask the Chatbot")
    st.info(
        "Ask me anything about personal finance, inflation, budgeting, or investments — "
        "in plain language! This is your smart financial companion. 🤖"
    )
    chat_page()

# 📊 Tab 2 – Visual Insights
with tab2:
    st.header("📊 Visual Insights: U.S. Inflation Trends")
    st.info(
        "See how inflation has changed over the years. Explore graphs that show the cost of living, "
        "how prices move, and what it means for your wallet. 📈"
    )
    render_visualization_tab()

# 🔔 Tab 3 – Alerts & Reminders
with tab3:
    st.header("🔔 Alerts & Reminders")
    st.info(
        "Never miss a bill, investment check-in, or retirement task. Set helpful reminders and alerts. "
        "Stay organized with peace of mind. ⏰"
    )
    alerts_reminders()

# 💼 Tab 4 – Safe Investment Simulator
with tab4:
    st.header("💼 Safe Investment Simulator")
    st.info(
        "Test different investment plans with simple sliders and get safe suggestions based on your comfort level. "
        "No risk — just learning. Try and see how your money can grow. 📊"
    )
    investment_simulator()

# 📚 Tab 5 – Resources
with tab5:
    st.header("📚 Helpful Resources")
    st.info(
        "Browse easy-to-read guides, trusted financial articles, and educational videos made for you. "
        "Because learning never stops. 📘"
    )
    resources_page()
