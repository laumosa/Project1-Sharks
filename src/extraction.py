import os
import pandas as pd



def open_df (name):
       
    # 1. Establish variables
    path = f"data/{name}.csv"
      
    # 2. We read from the path
    df = pd.read_csv(path, encoding='latin')
    
    return df