# Stock Analysis Tool

This tool provides simple stock analysis functionalities, including reading data from a CSV file, calculating Simple Moving Averages (SMA), and calculating Relative Strength Index (RSI).

## Usage

Here's a quick guide on how to use the tool in your Python script (`Assignment.py`):

```python
from stock_analysis_tool import read_csv, calculate_sma, calculate_rsi, write_to_csv

# Load data from a CSV file
file_path = 'orcl.csv'
data = read_csv(file_path)

# Calculate Simple Moving Averages (SMA) for a 5-day window
data_sma = calculate_sma(data, window=5)

# Calculate Relative Strength Index (RSI) for a 14-day window
data_rsi = calculate_rsi(data, window=14)

# Write SMA to orcl-sma.csv
data_sma_dict = [{'SMA_5': sma} for sma in data_sma]
write_to_csv(data_sma_dict, 'orcl-sma.csv')

# Write RSI to orcl-rsi.csv
data_rsi_dict = [{'RSI_14': rsi} for rsi in data_rsi]
write_to_csv(data_rsi_dict, 'orcl-rsi.csv')



## Installation

Install the package using pip:

```bash
pip install stock-analysis-tool

