#dfdc_vid_loc="/run/media/leenooks/Baiken/dfdc_train_all"
#dfdc_vid_loc="/run/media/leenooks/Baiken/dfdc_train_all"
#dfdc_vid_loc="/home/leenooks/Documents/Coding/AI_Proj/deepfake-detection-challenge/train_sample_videos"
#syms_py_script_loc="/home/leenooks/Documents/Coding/AI_Proj/DFDC-scripts/Test_Training_Validation_scripts/all_dfdc_split_videos.py"
#dfdc_syms_loc="/home/leenooks/Documents/Coding/AI_Proj/DFDC_syms"

dfdc_syms_loc="/home/leenooks/Documents/Coding/AI_Proj/prelim-syms"


headpose_step1_loc="/home/leenooks/Documents/Coding/AI_Proj/HeadPose/train_step1_landmarks.py"
headpose_step2_loc="/home/leenooks/Documents/Coding/AI_Proj/HeadPose/train_step2_headposes.py"
headpose_step3_loc="/home/leenooks/Documents/Coding/AI_Proj/HeadPose/train_step3_training.py"

headpose_landmark_loc="/home/leenooks/Documents/Coding/AI_Proj/HeadPose/step1/prelim1"
headpose_headpose_loc="/home/leenooks/Documents/Coding/AI_Proj/HeadPose/step2/prelim2"
headpose_final_model_loc="/home/leenooks/Documents/Coding/AI_Proj/HeadPose/final_models/prelim_dfdc_model"
headpose_run_loc="/home/leenooks/Documents/Coding/AI_Proj/HeadPose/run_test.py"
headpose_savefile_loc="/home/leenooks/Documents/Coding/AI_Proj/HeadPose/results/prelim_dfdc_split.pickle"






#echo $dfdc_vid_loc
#echo $dfdc_syms_loc

#python3 $syms_py_script_loc $dfdc_vid_loc $dfdc_syms_loc

python --version
#optirun python $headpose_step1_loc --real_video_dir=$dfdc_syms_loc/train/REAL --fake_video_dir=$dfdc_syms_loc/train/FAKE --output_landmark_path=$headpose_landmark_loc

sudo nice -n 5 optirun python $headpose_step2_loc --landmark_info_path=$headpose_landmark_loc --headpose_save_path=$headpose_headpose_loc

sudo nice -n 5 optirun python $headpose_step3_loc --headpose_path=$headpose_headpose_loc --model_save_path=$headpose_final_model_loc

sudo nice -n 5 python $headpose_run_loc --input_dir=$dfdc_syms_loc/test --classifier_path=$headpose_final_model_loc --save_file=$headpose_savefile_loc

