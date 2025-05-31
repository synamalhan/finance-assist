import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def investment_simulator():

    st.write("Answer these questions to find an investment style that fits you.")

    risk_tolerance = st.slider("How comfortable are you with investment risk?", 0, 10, 3)

    years = st.number_input("How many years do you plan to invest?", 1, 30, 10)

    initial_amount = st.number_input("Initial investment amount ($)", 1000, 100000, 10000)

    if st.button("Simulate"):
        # Simplified expected returns (annual %)
        portfolios = {
            "Conservative": 0.04,
            "Moderate": 0.07,
            "Aggressive": 0.12
        }

        projections = {}
        for style, rate in portfolios.items():
            final_value = initial_amount * ((1 + rate) ** years)
            projections[style] = final_value

        # Plot results
        fig, ax = plt.subplots()
        ax.bar(projections.keys(), projections.values(), color=['green', 'orange', 'red'])
        ax.set_ylabel("Projected Value ($)")
        ax.set_title(f"Investment Projection over {years} Years")
        st.pyplot(fig)

        # Text inference
        best_style = min(portfolios, key=lambda s: abs(portfolios[s] - (risk_tolerance/10)*0.12))
        st.write(f"Based on your risk comfort ({risk_tolerance}/10), a **{best_style}** portfolio might suit you best.")
