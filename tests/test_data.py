"""
This module contains tests for the fetch_data.py module.
Author: Asher Adighije

"""
import pytest
import os
import json
from src.fetch_data import load_data # Import the function to be tested

def test_load_data() -> None:
    """    
    Test that stock data loads correctly from the JSON file.

    Ensures:
        - The loaded data is a dictionary.
        - The expected structure exists within the JSON data.
        - There is at least one row of stock data.

    Raises:
        AssertionError: If any of the expected conditions fail.
    """
    data = load_data()
    
    # Ensure data is a dictionary
    assert isinstance(data, dict), "Data should be a dictionary"
    
    # Ensure the 'data' and 'tradesTable' keys exist
    assert "data" in data, "'data' key missing in loaded data"
    assert "tradesTable" in data["data"], "'tradesTable' key missing in loaded data"
    assert "rows" in data["data"]["tradesTable"], "'rows' key missing in trade table"
    
    # Ensure there are rows of data
    assert len(data["data"]["tradesTable"]["rows"]) > 0, "No stock data found"

def test_data_values() -> None:
    """
    Test that stock price values are correctly formatted.

    Ensures:
        - 'date' is a string.
        - 'close', 'open', 'high', and 'low' prices start with '$'.
        - 'volume' contains a comma for proper formatting.

    Raises:
        AssertionError: If any value does not meet the expected format.
    """
    data = load_data()
    rows = data["data"]["tradesTable"]["rows"]

    for row in rows[:5]:  # Test only the first 5 rows
        assert isinstance(row["date"], str), "Date should be a string"
        
        # Ensure numerical values are formatted correctly
        assert row["close"].startswith("$"), "Close price should start with '$'"
        assert row["open"].startswith("$"), "Open price should start with '$'"
        assert row["high"].startswith("$"), "High price should start with '$'"
        assert row["low"].startswith("$"), "Low price should start with '$'"
        assert "," in row["volume"], "Volume should be formatted with a comma"

def test_json_file_exists() -> None:
    """
    Ensure that the JSON data file exists after fetching data.

    This verifies that the fetch_data module correctly creates and saves the stock data file.

    Raises:
        AssertionError: If the JSON file is not found.
    """
    assert os.path.exists("data/aapl_data.json"), "JSON file not found"
