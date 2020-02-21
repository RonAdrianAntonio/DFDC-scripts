import os
import sys
import shutil
import pandas as pd
#import multiprocessing as mp
from multiprocessing import Pool

"""
This is for passing in multiple videos into FeatureExtraction, but all of the videos have a separate output folder for each of them as opposed to a single output folder for all of the frames

1st arg - FeatureExtraction binary location
2nd arg - directory w/ all of the folders with all of the folders of videos
3rd arg - destination folder root

"""
PROCESS_NUM = 3
RUN_FLAGS = "-aus -pose -2Dfp -3Dfp"

def run_openface(filename):
    folder_name = filename[:(len(filename) - 4)]


    global CURR_DIR 
    global FEAT_EXTR
    #print(CURR_DIR)
    #print(filename)
    dest_folder = CURR_DIR + "/" + os.path.split(folder_name)[1]
    os.mkdir(dest_folder)

    print(FEAT_EXTR + " -f " + filename + " -out_dir " + dest_folder + " " + RUN_FLAGS)
    #os.system(FEAT_EXTR + " -f " + filename + " -out_dir " + dest_folder + " " + RUN_FLAGS)
    


def create_results_dest(dest_loc):
    if os.path.exists(dest_loc):
        shutil.rmtree(dest_loc)

    os.mkdir(dest_loc)

    
    fake = dest_loc + "/FAKE"
    real = dest_loc + "/REAL"

    os.mkdir(fake)
    os.mkdir(real)


    return fake, real



def json_to_csv(json_loc):
    return pd.read_json(json_loc).T




def feat_extr():
    global FEAT_EXTR
    FEAT_EXTR = sys.argv[1]
    root_dir = sys.argv[2]
    dest_folder_root = sys.argv[3]


    fake_dir, real_dir = create_results_dest(dest_folder_root)


    locs = [x for x in os.listdir(root_dir) if os.path.isdir(root_dir + "/" + x)]

    #print(locs)
    for loc in locs:
        print(loc)

    global CURR_DIR
    for loc in locs:
        curr_folder = root_dir + "/" + loc

        curr_df = json_to_csv(curr_folder + "/metadata.json")

        fakes_df = curr_df[curr_df['label']=='FAKE']
        reals_df = curr_df[curr_df['label']=='REAL']

        fakes = [(curr_folder + "/" + x) for x in fakes_df.index.values.tolist()]
        reals = [(curr_folder + "/" + x) for x in reals_df.index.values.tolist()]

        #print(fakes)
        #print(reals)

        
        # Please uncomment the following two lines if you would like to separate each example by what part they were in (e.g. make a part_x folder
        # for every vid in part_x)
        CURR_DIR = real_dir #+ "/" + loc 
        #os.mkdir(CURR_DIR)

        with Pool(PROCESS_NUM) as pr:
            pr.map(run_openface, reals)

       
        CURR_DIR = fake_dir #+ "/" + loc
        #os.mkdir(CURR_DIR)
        with Pool(PROCESS_NUM) as pf:
            pf.map(run_openface, fakes)








        



if __name__ == "__main__":
    feat_extr()
