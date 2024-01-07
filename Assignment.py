import csv
from collections import deque
from stock_analysis_tool import read_csv, calculate_sma, calculate_rsi, write_to_csv

# Load data from a CSV file
file_path = 'your_stock_data.csv'
data = read_csv(file_path)

# Calculate Simple Moving Averages (SMA) for a 5-day window
data_sma = calculate_sma(data, window=5)

# Calculate Relative Strength Index (RSI) for a 14-day window
data_rsi = calculate_rsi(data, window=14)

# Write SMA to sma-results.csv
data_sma_dict = [{'SMA_5': sma} for sma in data_sma]
write_to_csv(data_sma_dict, 'sma-results.csv')

# Write RSI to rsi-results.csv
data_rsi_dict = [{'RSI_14': rsi} for rsi in data_rsi]
write_to_csv(data_rsi_dict, 'rsi-results.csv')
