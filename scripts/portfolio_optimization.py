import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def portfolio_analysis(tickers, weights, start_date='2020-01-01', risk_free_rate=0.02):
    """
    Performs portfolio analysis on a given list of tickers.
    
    Parameters:
    tickers (list): A list of stock tickers (e.g., ['AAPL', 'GOOGL', 'MSFT']).
    weights (dict): A dictionary of asset weights corresponding to the tickers.
    start_date (str): The start date for the analysis (default is '2020-01-01').
    risk_free_rate (float): The risk-free rate used for Sharpe ratio calculation (default is 0.02).
    
    Returns:
    dict: A dictionary with portfolio metrics: expected return, volatility, and Sharpe ratio.
    """
    
    # Fetch historical stock data
    stock_data = yf.download(tickers, start=start_date)['Adj Close']
    
    # Calculate daily returns
    daily_returns = stock_data.pct_change().dropna()
    
    # Calculate portfolio returns
    portfolio_returns = (daily_returns * np.array(list(weights.values()))).sum(axis=1)
    
    # Calculate expected return and volatility (annualized)
    expected_return = portfolio_returns.mean() * 252  # Assuming 252 trading days in a year
    volatility = portfolio_returns.std() * np.sqrt(252)  # Annualized volatility
    
    # Calculate Sharpe Ratio
    sharpe_ratio = (expected_return - risk_free_rate) / volatility
    
    # Portfolio performance visualization
    plt.figure(figsize=(10, 6))
    portfolio_returns.cumsum().plot(label='Portfolio Growth', color='blue')
    plt.title("Portfolio Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.show()
    
    # Return portfolio metrics
    return {
        'Expected Return': expected_return,
        'Volatility': volatility,
        'Sharpe Ratio': sharpe_ratio
    }


