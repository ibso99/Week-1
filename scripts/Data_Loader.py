import pandas as pd 

def Data_Loader(file_path):
    ''' creating a 
    dataloader function '''
    return pd.read_csv(file_path, parse_dates=['Date'])