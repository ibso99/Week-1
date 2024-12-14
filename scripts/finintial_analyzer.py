import talib as ta
import pandas as pd
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
import plotly.express as px


class FinancialAnalyzer:
    def __init__(self, data_path, start_date=None, end_date=None):
        self.data_path = data_path
        self.start_date = pd.to_datetime(start_date) if start_date else None
        self.end_date = pd.to_datetime(end_date) if end_date else None
        self.data = None

    def retrieve_data(self):
        '''Loads the data and filters it by date range.'''
        # Load data
        self.data = pd.read_csv(self.data_path)
        
        # Ensure the 'Date' column is datetime
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        
        # Filter by date range if provided
        if self.start_date and self.end_date:
            self.data = self.data[(self.data['Date'] >= self.start_date) & (self.data['Date'] <= self.end_date)]
        
        # Sort by date (optional, but helpful for time-series analysis)
        self.data = self.data.sort_values('Date').reset_index(drop=True)
        
        return self.data

    def calculate_technical_indicator(self):
        '''Calculates technical indicators: SMA, RSI, and EMA.'''
        if self.data is None:
            raise ValueError("Data not loaded. Call retrieve_data() first.")
        
        # Calculate Simple Moving Average (SMA)
        self.data['SMA'] = ta.SMA(self.data['Close'], timeperiod=20)
        
        # Calculate Relative Strength Index (RSI)
        self.data['RSI'] = ta.RSI(self.data['Close'], timeperiod=14)
        
        # Calculate Exponential Moving Average (EMA)
        self.data['EMA'] = ta.EMA(self.data['Close'], timeperiod=20)

        macd, macd_signal, macd_hist = ta.MACD(self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        self.data['MACD'] = macd
        self.data['MACD_Signal'] = macd_signal
        self.data['MACD_Hist'] = macd_hist
            
        return self.data

    def plot_stock_data(self, data):
        fig = px.line(data, x=data.index, y=['Close', 'SMA'], 
                      title="Stock Closing Price With Moving Average")
        fig.show()
    
    def plot_rsi(self, data):
        fig = px.line(data, x=data.index, y='RSI', 
                      title="Relative Strength Index (RSI)")
        fig.show()

    def plot_ema(self, data):
        fig = px.line(data, x=data.index, y=['Close', 'EMA'], 
                      title="Stock Closing Price With Exponential Moving Average")
        fig.show()

    def plot_macd(self, data):
        fig = px.line(data, x=data.index, y=['MACD', 'MACD_Signal'], 
                      title="Moving Average Convergence Divergence")
        fig.show()

    def calculate_portfolio_weights(self, data_path, start_date, end_date):
        data = pd.read_csv(data_path)
        data['Date'] = pd.to_datetime(data['Date'])
        data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
        mu = expected_returns.mean_historical_return(data)
        cov = risk_models.sample_cov(data)
        ef = EfficientFrontier(mu, cov)
        weights = ef.max_sharpe()
        weights = dict.zip(_,weights.values())
        return weights
    
    
    def calculate_portfolio_performance(self,data):
        price_data = data[['Close']]
        returns = price_data.pct_change().dropna()
        mu = expected_returns.mean_historical_return(returns)
        cov = risk_models.sample_cov(returns)
        ef = EfficientFrontier(mu, cov)
        weights = ef.max_sharpe()
        portfolio_return, portfolio_volatility, sharpe_ratio = ef.portfolio_performance()
        return portfolio_return, portfolio_volatility, sharpe_ratio
        
    