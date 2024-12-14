import pandas as pd 

AAPL_PATH = "C:\Users\ibsan\Desktop\TenX\week-1\Data\yfinance_data\AAPL_historical_data.csv"
AMZN_PATH = "C:\Users\ibsan\Desktop\TenX\week-1\Data\yfinance_data\AMZN_historical_data.csv"
GOOG_PATH = "C:\Users\ibsan\Desktop\TenX\week-1\Data\yfinance_data\GOOG_historical_data.csv"
META_PATH = "C:\Users\ibsan\Desktop\TenX\week-1\Data\yfinance_data\META_historical_data.csv"
MSFT_PATH = "C:\Users\ibsan\Desktop\TenX\week-1\Data\yfinance_data\MSFT_historical_data.csv"
NVDA_PATH = "C:\Users\ibsan\Desktop\TenX\week-1\Data\yfinance_data\NVDA_historical_data.csv"
TSLA_PATH = "C:\Users\ibsan\Desktop\TenX\week-1\Data\yfinance_data\TSLA_historical_data.csv"

AAPL_DF = pd.read_csv(AAPL_PATH)
AMZN_DF = pd.read_csv(AMZN_PATH)
GOOG_DF = pd.read_csv(GOOG_PATH)
META_DF = pd.read_csv(META_PATH)
MSFT_DF = pd.read_csv(MSFT_PATH)
NVDA_DF = pd.read_csv(NVDA_PATH)
TSLA_DF = pd.read_csv(TSLA_PATH)