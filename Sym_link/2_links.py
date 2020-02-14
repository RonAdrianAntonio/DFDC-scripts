import pandas as pd
import re
import os
import sys
import shutil

"""

1st argument = root directory of Celeb-DF
2nd argument = csv filename to be used
3rd argument = new folder name for results

"""

def link():
    root_dir = sys.argv[1]
    csv = pd.read_csv(root_dir + "/Celeb-DF/CSVs/" + sys.argv[2])
    
    results_loc = root_dir + "/Celeb-DF/frames-grouped/" + sys.argv[3]
    
    if os.path.exists( results_loc ):
        shutil.rmtree(results_loc)
        
    os.mkdir(results_loc)
    
    for index, row in csv.iterrows():
        curr_path = root_dir + "/" + row['local_path']
        curr_folder = results_loc + "/" + row['src_video_name'] + "-folder"
        if not os.path.exists(curr_folder):
            os.mkdir(curr_folder)
            
        os.copyfile(curr_path, curr_folder + "/" + row['frame_name'])
            
        
        
            
        
            
    """
    for (curr_directory_path, directories, files) in os.walk("."):
        for f in files:
            if ".csv" in f:
                csvs[f] = pd.read_csv(f)
    file_num = 1 
    for (curr_directory_path, directories, files) in os.walk(sys.argv[1]):
        for f in files:
            if ".mp4" in f:
                split_dir = curr_directory_path.split('/')
                csv_loc = split_dir[len(split_dir) - 1] + ".csv"
                curr_csv = csvs[csv_loc]
                #print(curr_csv)
                curr_row = curr_csv[curr_csv.iloc[:,0].str.contains(f)]

                print(file_num, curr_row)
                curr_row_label = curr_row['label'].values[0]

                os.symlink(curr_directory_path + '/' + f, curr_row_label + "/" + f + ".slnk")
                file_num += 1
    
    """



if __name__ == "__main__":
    link()
