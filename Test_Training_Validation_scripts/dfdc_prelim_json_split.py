import os
import sys
import shutil
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


TEST_SIZE = 0.1



def create_syms(filename_list, origin_root, dest_root):

    for name in filename_list:
        os.symlink(origin_root + "/" + name, dest_root + "/" + name + ".lnk") 



def replace_syms(folder):
    replace_folder(folder)
    os.mkdir(folder + "/train")
    os.mkdir(folder + "/test")
    os.mkdir(folder + "/train/REAL")
    os.mkdir(folder + "/train/FAKE")
    os.mkdir(folder + "/test/REAL")
    os.mkdir(folder + "/test/FAKE")
    os.mkdir(folder + "/test/ALL")

def replace_folder(folder):

    if os.path.exists(folder):
        shutil.rmtree(folder)


    os.mkdir(folder)
    

def split_videos():
    dfdc_loc = sys.argv[1]
    dest_loc = sys.argv[2]

    replace_syms(dest_loc)

    metadata_files = []
    for root, _, filenames in os.walk(dfdc_loc):
        for f in filenames:
            if f == 'metadata.json':
                metadata_files.append(os.path.join(root, f))

    
    #print(metadata_files)
    for file in metadata_files:
        print(file)
        metadata_root, _ = os.path.split(file) 

        df = pd.read_json(file).T
        #print(df)
        #print(df[df['label']=='FAKE'])
        fake_df = df[df['label']=='FAKE']
        real_df = df[df['label']=='REAL']

        #print(fake_df.index)
        #print(real_df.index) 
        #print(type(fake_df.index))
        #print(type(real_df.index)) 

        fake_idx_list = fake_df.index.tolist() 
        real_idx_list = real_df.index.tolist() 

        print("Fake Split\n\n")
        fake_split = train_test_split(fake_idx_list, test_size = TEST_SIZE, random_state=31)
        #print(fake_split)

        create_syms(fake_split[0], metadata_root, dest_loc + "/train/FAKE")
        create_syms(fake_split[1], metadata_root, dest_loc + "/test/FAKE")
        create_syms(fake_split[1], metadata_root, dest_loc + "/test/ALL")
        print("Created Fake split")


    
        print("Real Split\n\n")
        real_split = train_test_split(real_idx_list, test_size = TEST_SIZE, random_state=31)
        #print(real_split)


        create_syms(real_split[0], metadata_root, dest_loc + "/train/REAL")
        create_syms(real_split[1], metadata_root, dest_loc + "/test/REAL")
        create_syms(real_split[1], metadata_root, dest_loc + "/test/ALL")
        print("Created Real Split")
        




if __name__ == "__main__":
    split_videos()

