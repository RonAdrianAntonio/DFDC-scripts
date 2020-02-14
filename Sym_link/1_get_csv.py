import pandas as pd
import re
from os import walk
import sys

def from_json_to_csv():
    jsons = {}

    for (curr_directory_path, directories, files) in walk(sys.argv[1]):
        for f in files:
            whole_path = curr_directory_path + "/" + f
            if ".json" in f:
                prev_dir_list = curr_directory_path.split('/')
                prev_dir = prev_dir_list[len(prev_dir_list)-1]
                jsons[prev_dir] = pd.read_json("file://" + whole_path).T
                print(whole_path)


    for key in jsons.keys():
        
        jsons[key].to_csv(key + ".csv")
        

if __name__ == "__main__":
    from_json_to_csv()
