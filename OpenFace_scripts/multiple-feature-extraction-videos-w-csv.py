import os
import sys
import shutil
import pandas as pd

"""
This is for passing in multiple videos into FeatureExtraction, but all of the videos have a separate folder for each of them as opposed to a single output folder for all of the frames

1st arg - directory w/ all of the folders with all of the pictures
2nd arg - destination folder root

"""

def feat_extr():
    root_dir = sys.argv[1]
    dest_folder_root = sys.argv[2]

    locs_df = pd.read_csv(root_dir + "/dataset.csv")

    if os.path.exists(dest_folder_root):
        shutil.rmtree(dest_folder_root)

    os.mkdir(dest_folder_root)

    fake_dir = dest_folder_root + "/fake"
    real_dir = dest_folder_root + "/real"

    os.mkdir(fake_dir)
    os.mkdir(real_dir)

    for idx, row in locs_df.iterrows():
        if row['label'] == 1:
            dest_folder = fake_dir
        else:
            dest_folder = real_dir

#        print(idx)
 #       print(row)

        split_name = row['Unnamed: 0'].split("/")
        #print(split_name)

        
        folder_name = split_name[0] + "__" + split_name[len(split_name)-1]

        os.mkdir(dest_folder + "/" + folder_name)


        os.system("./FeatureExtraction -f " + root_dir + "/" + row['Unnamed: 0'] + " -out_dir " + dest_folder + "/" + folder_name + " -aus -pose -2Dfp -3Dfp")









        



if __name__ == "__main__":
    feat_extr()
