import streamlit as st
import pandas as pd
from fetch_data import load_data

st.title("Statistics View 📊")

data = load_data()

if data and "data" in data and "tradesTable" in data["data"]:
    table_data = data["data"]["tradesTable"]["rows"]

    # Convert to Pandas DataFrame
    df = pd.DataFrame(table_data)
    
    # Convert numeric columns
    df["close"] = df["close"].str.replace("$", "").astype(float)
    df["open"] = df["open"].str.replace("$", "").astype(float)
    df["high"] = df["high"].str.replace("$", "").astype(float)
    df["low"] = df["low"].str.replace("$", "").astype(float)
    df["volume"] = df["volume"].str.replace(",", "").astype(int)

    # Display statistics
    st.subheader("Stock Price Summary")
    st.write(df.describe())  # Show summary statistics

    # Show highest and lowest closing prices
    highest_close = df.loc[df["close"].idxmax()]
    lowest_close = df.loc[df["close"].idxmin()]

    st.subheader("📈 Highest Closing Price")
    st.write(highest_close)

    st.subheader("📉 Lowest Closing Price")
    st.write(lowest_close)

else:
    st.error("No data available.")

