# visualization.py
import streamlit as st
import matplotlib.pyplot as plt
from fred_data import fetch_fred_data as fred_data
import pandas as pd
# visualization.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from fred_data import fetch_fred_data as fred_data

# Mapping for user-friendly selection
indicator_options = {
    "U.S. Gross National Product": "GNPCA",
    "Consumer Price Index (CPI)": "CPIAUCSL",
    "Unemployment Rate": "UNRATE",
    "Federal Funds Rate": "FEDFUNDS",
    "Personal Savings Rate": "PSAVERT"
}

# Friendly descriptions for each economic indicator
indicator_descriptions = {
    "U.S. Gross National Product": "Measures the total economic output of the U.S., helping you understand how the economy is growing over time.",
    "Consumer Price Index (CPI)": "Tracks the average change in prices paid by consumers for goods and services. Helps you see inflation trends.",
    "Unemployment Rate": "Shows the percentage of people who are looking for jobs but can’t find one. Useful for understanding job market conditions.",
    "Federal Funds Rate": "The interest rate at which banks lend to each other. Influences loan rates, mortgages, and savings interest.",
    "Personal Savings Rate": "Shows how much of their income people in the U.S. are saving. Useful for understanding consumer financial behavior."
}


time_range_options = {
    "Last 5 Years": "2019-01-01",
    "Last 10 Years": "2014-01-01",
    "Since 2000": "2000-01-01"
}

# Practical inferences for each indicator
indicator_inferences = {
    "U.S. Gross National Product": (
        "If this number is rising, it means the economy is growing, which often means more jobs and better financial opportunities. "
        "If it’s falling, the economy may be slowing down."
    ),
    "Consumer Price Index (CPI)": (
        "A rising CPI means prices are going up (inflation), so everyday things like groceries or gas might cost more. "
        "If it’s steady or falling, prices are stable or decreasing."
    ),
    "Unemployment Rate": (
        "A low unemployment rate means more people have jobs, which is good for the economy and community wellbeing. "
        "A high rate might mean jobs are harder to find."
    ),
    "Federal Funds Rate": (
        "When this interest rate is low, borrowing money (like loans or mortgages) is cheaper, but savings earn less interest. "
        "A higher rate can slow borrowing but help savings grow."
    ),
    "Personal Savings Rate": (
        "A higher savings rate means people are setting aside more money for emergencies or retirement, which is good for financial security."
    )
}

def render_visualization_tab():

    selected_indicator = st.selectbox("Select an Economic Indicator", list(indicator_options.keys()))
    selected_range = st.selectbox("Select a Time Range", list(time_range_options.keys()))

    # Show description
    st.info(indicator_descriptions[selected_indicator])

    if st.button("Show Data Visualization"):
        try:
            series_id = indicator_options[selected_indicator]
            start_date = time_range_options[selected_range]

            df = fred_data(series_id, start_date)
            st.success("Here's the chart!")

            st.line_chart(df.set_index("date")["value"])
            st.caption(f"Data Source: FRED - {selected_indicator}")

            # Show inference
            st.markdown("### What This Means for You")
            st.write(indicator_inferences[selected_indicator])

        except Exception as e:
            st.error(f"Error: {e}")
