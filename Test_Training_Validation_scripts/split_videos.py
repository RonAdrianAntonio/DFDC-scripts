import os
import sys
import shutil
from sklearn.model_selection import KFold
import numpy as np
import pandas as pd

def replace_folder(folder):

    if os.path.exists(folder):
        shutil.rmtree(folder)


    os.mkdir(folder)

def split_videos():
    train_loc = sys.argv[1]
    dest_loc = sys.argv[2]

    metadata_loc = train_loc + "/metadata.json"

    metadata = pd.read_json(metadata_loc).T

    #print(metadata)
    
     
    videos_arr = os.listdir(train_loc)
    videos_arr.remove("metadata.json")
    #print(videos_arr)

    videos_X = np.array(videos_arr)
    videos_Y = []

    #print(metadata.index.values)

    for filename in videos_arr:
        videos_Y.append(1 if metadata.loc[filename]['label']=="FAKE" else 0)

    #print(videos_Y)
    videos_Y = np.array(videos_Y)

    kfold_master = KFold()

    master_iters = 0

    for train_idx, test_idx in kfold_master.split(videos_X):
        master_iter_folder = dest_loc + "/" + str(master_iters)

        replace_folder(master_iter_folder)
        
        train_master, test_master =  videos_X[train_idx], videos_X[test_idx]

        master_iter_folder_test = master_iter_folder + "/" + "test"

        os.mkdir(master_iter_folder_test)

        for test_filename in test_master:
            shutil.copyfile(train_loc + "/" + test_filename, master_iter_folder_test + "/" + test_filename)


        master_iter_folder_train = master_iter_folder + "/" + "train"

        os.mkdir(master_iter_folder_train)

        for filename in train_child:
            shutil.copyfile(train_loc + "/" + filename, master_iter_folder_train + "/" + filename)


        master_iters += 1


        




"""

    kfold = KFold()

    for train_idx, test_idx in kfold.split(videos_np):
        #print(train_idx)
        #print(test_idx)
        print("df")

"""







if __name__ == "__main__":
    split_videos()

