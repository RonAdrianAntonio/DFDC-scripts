import pandas as pd
import re
import os
import sys
import shutil

"""

1st argument = location of json file
2nd argument = root directory of json file locations
3rd argument = new folder name for results

"""

def link():
    metadata = pd.read_json(sys.argv[1]).T
    root_dir = sys.argv[2]

    dest_dir = sys.argv[3]

    
   
    if os.path.exists( dest_dir ):
        shutil.rmtree(dest_dir)
        
    os.mkdir(dest_dir)

    train_dir = dest_dir + "/" + "train"
    test_dir = dest_dir + "/" + "test"

    train_real_dir = train_dir + "/" + "REAL"
    train_fake_dir = train_dir + "/" + "FAKE"

    os.mkdir(train_dir)
    os.mkdir(test_dir)
    os.mkdir(train_real_dir)
    os.mkdir(train_fake_dir)
    
    #print(metadata)

    #print(metadata[['label', 'set']])

    #print(metadata.index.values.tolist())

  
    metadata_tup = [(idx, metadata[['label', 'set']].loc[idx].values.tolist()[0], metadata[['label', 'set']].loc[idx].values.tolist()[1]) for idx in metadata.index.values.tolist()]

    for x in metadata_tup:
        #print('owo')
        #print(x)
        #print('whats this')
        if x[2] == 'train':
            if x[1] == 'fake':
                os.symlink(root_dir + "/" + x[0], train_fake_dir + "/" + x[0].replace('/', '_')+ '.lnk')
            else:
                os.symlink(root_dir + "/" + x[0], train_real_dir + "/" + x[0].replace('/', '_')+ '.lnk')
        else:
            os.symlink(root_dir + "/" + x[0], test_dir + "/" + x[1] + "_" + x[0].replace('/', '_') + '.lnk')
    

    """
    for index, row in csv.iterrows():
        curr_path = root_dir + "/" + row['local_path']
        curr_folder = results_loc + "/" + row['src_video_name'] + "-folder"
        if not os.path.exists(curr_folder):
            os.mkdir(curr_folder)
            
        os.copyfile(curr_path, curr_folder + "/" + row['frame_name'])
            
        
        
    """        
        
            
  


if __name__ == "__main__":
    link()
