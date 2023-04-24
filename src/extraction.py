import os
import pandas as pd

def open_df (name):
    """This code defines a function called extraction that takes a name argument, sets a file path based on the name argument, 
    reads a CSV file from that path and returns the DataFrame.
    """
    
    # 1. Establish variables
    path = f"data/{name}.csv"
      
    # 2. We read from the path
    df = pd.read_csv(path, encoding='latin')
    
    return df