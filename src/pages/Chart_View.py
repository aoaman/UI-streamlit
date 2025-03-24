import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fetch_data import load_data

st.title("Chart View 📈")

data = load_data()

if data and "data" in data and "tradesTable" in data["data"]:
    table_data = data["data"]["tradesTable"]["rows"]

    # Convert to Pandas DataFrame
    df = pd.DataFrame(table_data)
    
    # Convert columns to appropriate types
    df["date"] = pd.to_datetime(df["date"])
    df["close"] = df["close"].str.replace("$", "").astype(float)

    # Plot Close Prices over time
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["close"], marker="o", linestyle="-", label="Close Price")
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price (USD)")
    ax.set_title("AAPL Stock Price Over Time")
    ax.legend()

    st.pyplot(fig)
else:
    st.error("No data available.")
