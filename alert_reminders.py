import streamlit as st
from datetime import datetime

def alerts_reminders():
    st.header("🔔 Alerts & Reminders")
    today = datetime.today().date()

    # Hardcoded important dates (can later be loaded from a database or API)
    important_dates = {
        "Tax filing deadline": "2025-04-15",
        "Medicare Open Enrollment": "2025-10-15",
        "Social Security Benefit Increase Announcement": "2025-11-01"
    }

    for event, date_str in important_dates.items():
        event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        days_left = (event_date - today).days
        if days_left >= 0:
            st.info(f"{event}: {date_str} — {days_left} days left")
        else:
            st.success(f"{event}: {date_str} — Passed")

    # User personal reminders (optional)
    st.subheader("Set a personal reminder")
    reminder_date = st.date_input("Reminder date")
    reminder_text = st.text_input("Reminder note")
    if st.button("Save Reminder"):
        st.success(f"Reminder set for {reminder_date}: {reminder_text}")
