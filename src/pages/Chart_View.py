import streamlit as st
import pandas as pd
from fetch_data import load_data

def chart_view():
    """
    Display stock data using Streamlit's built-in charting functions.
    """
    st.title("Stock Data - Chart View")

    data = load_data()
    if not data:
        st.error("No data available. Please fetch the latest stock data.")
        return

    # Convert data to a DataFrame
    rows = data["data"]["tradesTable"]["rows"]
    df = pd.DataFrame(rows)

    # Convert numeric values
    df["date"] = pd.to_datetime(df["date"])
    df["close"] = df["close"].str.replace("$", "").astype(float)
    df = df.sort_values("date")

    # Use Streamlit's built-in line chart
    st.line_chart(df.set_index("date")["close"])

if __name__ == "__main__":
    chart_view()
