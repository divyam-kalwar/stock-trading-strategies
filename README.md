# Stock Trading Strategy Project

## Overview
This project implements a stock trading strategy based on moving averages. It loads historical stock data from a PostgreSQL database, generates trading signals, calculates profit and loss (PnL), and visualizes the trading data using candlestick charts. The strategy is based on the crossover of short-term and long-term moving averages.

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/divyam-kalwar/stock-trading-strategies

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Ensure you have PostgreSQL installed and running on your system. You can download PostgreSQL from the official website.

## Usage
1. Set up your PostgreSQL database and import historical stock data for the desired stocks. Ensure each stock's data is stored in a separate table in the database.
2. Update the database connection details in the database_operations.py file with your PostgreSQL database credentials.
3. Run the main.py script to execute the trading strategy:
   ```bash
   python main.py
   
## Project Structure
* main.py: Main script that orchestrates the entire trading strategy.
* trading_signals.py: Module containing functions to generate trading signals based on moving averages.
* pnl_calculation.py: Module containing functions to calculate profit and loss (PnL) for trades.
* database_operations.py: Module containing functions to interact with the PostgreSQL database, including loading data and storing PnL data.
* visualization.py: Module containing functions to visualize trading data using candlestick charts.
* requirements.txt: File containing the list of Python dependencies required for the project.

## Database Setup
1. Set up a PostgreSQL database.
2. Import historical stock data into separate tables for each stock.
3. Ensure each table contains columns for date, open, high, low, close, adjusted close, and volume.
