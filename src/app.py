import streamlit as st
from fetch_data import load_data

st.set_page_config(page_title="APPL Stock Data", layout="wide")


st.sidebar.title("Navigation")
st.sidebar.page_link("pages/Table_View.py", label="Table View")
st.sidebar.page_link("pages/Chart_View.py", label="Chart View")
st.sidebar.page_link("pages/Statistics_View.py", label="Statistics View")

st.title("Welcome to the AAPL Stock Data Viewer! 📊")
st.write("Use the sidebar to navigate through different views of the stock data.")
