"""
Table View Page
Author: Asher Adighije
"""
import streamlit as st
from fetch_data import load_data

st.title("Table View 📊")

data = load_data()

if data and "data" in data and "tradesTable" in data["data"]:
    table_data = data["data"]["tradesTable"]["rows"]
    st.dataframe(table_data)
else:
    st.error("No data available.")

