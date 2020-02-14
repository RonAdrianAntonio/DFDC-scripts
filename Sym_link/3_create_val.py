import pandas as pd
import re
import os
import sys
import shutil

def sym_link():
    

    csvs = {}
    fake_list = os.listdir("FAKE")
    real_list = os.listdir("REAL")
        
    print(len(fake_list))
    print(len(real_list))
"""
    for (curr_directory_path, directories, files) in os.listdir("FAKE"):
        for f in files:
            if ".csv" in f:
                csvs[f] = pd.read_csv(f)

    for (curr_directory_path, directories, files) in os.listdir("FAKE"):
        for f in files:
            if ".csv" in f:
                csvs[f] = pd.read_csv(f)
    
            
"""

            
            
            
      
            



if __name__ == "__main__":
    sym_link()
