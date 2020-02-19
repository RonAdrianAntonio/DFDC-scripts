#!/bin/bash
#cp /run/media/leenooks/Baiken/dfdc_train_all.zip /run/media/leenooks/BIGGESTBOI
unzip /run/media/leenooks/Baiken/dfdc_train_all.zip -d /run/media/leenooks/Baiken/dfdc_train_all/

#for zip_name in /home/leenooks/Documents/College/Books/Yr3/*
for zip_name in /run/media/leenooks/Baiken/dfdc_train_all/*
do
    echo $zip_name 

    folder_name=$(echo ${zip_name:0:60})
    mkdir $folder_name
    unzip $zip_name -d $folder_name
     
done

