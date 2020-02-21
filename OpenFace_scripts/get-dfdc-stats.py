import os
import sys
import shutil
import pandas as pd
#import multiprocessing as mp
from multiprocessing import Pool

"""
This is for passing in multiple videos into FeatureExtraction, but all of the videos have a separate output folder for each of them as opposed to a single output folder for all of the frames

1st arg - directory w/ all of the folders with all of the folders of videos

"""




def json_to_csv(json_loc):
    return pd.read_json(json_loc).T




def feat_extr():
    root_dir = sys.argv[1]



    locs = [x for x in os.listdir(root_dir) if os.path.isdir(root_dir + "/" + x)]


    fake_percents = []
    real_percents = []
    
    unique_sources = set()
    for loc in locs:
        print(loc)
        curr_folder = root_dir + "/" + loc


        curr_df = json_to_csv(curr_folder + "/metadata.json")

        fakes_df = curr_df[curr_df['label']=='FAKE']
        reals_df = curr_df[curr_df['label']=='REAL']

        fakes = [(curr_folder + "/" + x) for x in fakes_df.index.values.tolist()]
        reals = [(curr_folder + "/" + x) for x in reals_df.index.values.tolist()]

        fake_num = len(fakes)
        real_num = len(reals)
        all_num = fake_num + real_num

        fake_pc = float(fake_num) / float(all_num)
        real_pc = float(real_num) / float(all_num)

        print("Total Fakes:", len(fakes))
        print("Total Reals:", len(reals))

        print("Percentage of Fakes: {0:.2f}%".format( fake_pc ))
        print("Percentage of Reals: {0:.2f}%".format( real_pc ))

        fake_percents.append(fake_pc)
        real_percents.append(real_pc)


        sources = curr_df[['original']].dropna().T.values.tolist()[0]

        #print(sources)
        for val in sources:
            unique_sources.add(val)

    
    fake_pc_avg = sum(fake_percents) / float(len(fake_percents))
    real_pc_avg = sum(real_percents) / float(len(real_percents))

    
        
    print("\n\n\n\nAverage Percentage of Fakes: {0:.2f}%".format( fake_pc_avg ))
    print("Average Percentage of Reals: {0:.2f}%".format( real_pc_avg ))

    print("Number of unique sources:", len(unique_sources))

        

        


        





        



if __name__ == "__main__":
    feat_extr()
