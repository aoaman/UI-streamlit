import streamlit as st
import pandas as pd
from fetch_data import load_data

def chart_view():
    """
    Display stock data using Streamlit's built-in charting functions with a year range filter.
    """
    st.title("Stock Data - Chart View")

    data = load_data()
    if not data:
        st.error("No data available. Please fetch the latest stock data.")
        return

    # Convert data to a DataFrame
    rows = data["data"]["tradesTable"]["rows"]
    df = pd.DataFrame(rows)

    # Convert date and numeric values
    df["date"] = pd.to_datetime(df["date"])
    df["close"] = df["close"].str.replace("$", "").astype(float)
    df = df.sort_values("date")

    # Get unique years from the data for the user to select
    min_year = df["date"].dt.year.min()
    max_year = df["date"].dt.year.max()

    # Let the user select the year range for filtering
    start_year, end_year = st.slider(
        "Select the year range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        step=1
    )

    # Filter data based on selected year range
    filtered_df = df[(df["date"].dt.year >= start_year) & (df["date"].dt.year <= end_year)]

    # Use Streamlit's built-in line chart
    st.line_chart(filtered_df.set_index("date")["close"])

if __name__ == "__main__":
    chart_view()


