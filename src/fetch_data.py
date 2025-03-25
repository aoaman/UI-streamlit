"""
This module fetches and caches stock data from the NASDAQ API.
Author: Asher Adighije
"""
import os
import json
import requests
import streamlit as st

DATA_FILE = "data/aapl_data.json"
API_URL = "https://api.nasdaq.com/api/quote/AAPL/historical?assetclass=stocks&fromdate=2020-02-05&limit=9999"

def download_data() -> dict | None:
    """
    Fetch stock data from the NASDAQ API and save it locally.

    Returns:
        dict: The fetched stock data if successful.
        None: If an error occurs during the fetch or if the data format is invalid.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(API_URL, headers=headers, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Ensure the 'data' key exists and contains the expected structure
        if "data" in data and "tradesTable" in data["data"] and "rows" in data["data"]["tradesTable"]:
            # Create the data directory if it doesn't exist
            os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

            # Save the data
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            return data  # Return the data for immediate use
        else:
            st.error("Error: Unexpected data format received from API.")
            return None

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

@st.cache_data(ttl=60*10)  # Cache the data for 10 minutes
def load_data() -> dict | None:
    """
    Load stock data from the local JSON file. If missing, fetch from the API.

    Returns:
        dict: The stock data if successfully loaded.
        None: If the file is missing, corrupt, or cannot be loaded properly.
    """
    if not os.path.exists(DATA_FILE):
        st.warning("No local data found. Fetching from API...", icon="⏳")
        return download_data()
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        st.error("Error decoding JSON file.")
        return None

