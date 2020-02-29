#!/bin/bash
import pandas as pd
import os
import sys

root_folder = sys.argv[1]
dest_folder = sys.argv[2]



for folder in os.listdir(root_folder):
    root_loc = root_folder + "/" + folder + "/metadata.json"


    if 'all_metadata' in globals():
        curr_metadata = pd.read_json(root_loc).T
        curr_metadata['original_part'] = folder
        all_metadata = pd.concat([all_metadata, curr_metadata])

    else:
        all_metadata = pd.read_json(root_loc).T
        all_metadata['original_part'] = folder


all_metadata.to_csv(dest_folder + '/all_metadata.csv')





