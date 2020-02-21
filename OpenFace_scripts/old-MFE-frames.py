import os
import sys
import shutil

"""
This is for passing in multiple videos into FeatureExtraction, but all of the videos have a separate folder for each of them as opposed to a single output folder for all of the frames

1st arg - directory w/ all of the folders with all of the pictures
2nd arg - destination folder root

"""

def feat_extr():
    root_dir = sys.argv[1]
    dest_folder_root = sys.argv[2]

    for loc in os.listdir(root_dir):
        dest_folder = dest_folder_root + "/" + loc

        if os.path.exists(dest_folder):
            shutil.rmtree(dest_folder)


        os.mkdir(dest_folder)
        os.system("sudo ./FeatureExtraction -fdir " + root_dir + "/" + loc + " -out_dir " + dest_folder)

if __name__ == "__main__":
    feat_extr()
