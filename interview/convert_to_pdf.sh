#!/usr/bin/bash

folder_name=$1
# output_name=$2
BASE_PATH="/mnt/c/Users/bduy1/OneDrive/JOBs/Interview"
img2pdf=$(which img2pdf)

python3 download_img.py --file file.html --output $folder_name
# run (numeric sort so 1.jpg, 2.jpg ... are in order)
ls -1v $folder_name/*.jpg | xargs img2pdf -o $BASE_PATH/$folder_name.pdf