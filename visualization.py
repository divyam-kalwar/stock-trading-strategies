import matplotlib.pyplot as plt
import pandas as pd
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates

def visualize_trading_data(df, symbol):
    # Convert date to matplotlib date format
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].apply(mdates.date2num)
    # Create subplots with shared x-axis
    fig, ax = plt.subplots(figsize=(10, 6))
    # Plot candlestick chart
    candlestick_ohlc(ax, df[['date', 'open', 'high', 'low', 'close']].values, width=0.6, colorup='g', colordown='r',
                     alpha=0.8)
    # Plot buy signals
    ax.plot(df[df['signal'] == 1]['date'], df[df['signal'] == 1]['close'], '^', markersize=10, color='g',
            label='Buy Signal')
    # Plot sell signals
    ax.plot(df[df['signal'] == -1]['date'], df[df['signal'] == -1]['close'], 'v', markersize=10, color='r',
            label='Sell Signal')
    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title(f'Trading Data for {symbol}')
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Set date format for x-axis
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Adjust date format as needed

    # Add legend
    ax.legend()
    # Show plot
    plt.show()