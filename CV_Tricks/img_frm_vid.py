#!/usr/bin/env python
import os
import cv2
import argparse

def img_frm_video (video_name,save_dir):
	cap = cv2.VideoCapture(video_name)
	print('Reading video file')
	ret, img = cap.read()
	count = 1
	while ret:
		cv2.imwrite(os.path.join(save_dir,'image%d.jpg' %count), img)
		ret, img = cap.read()
		count += 1

if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", required=True, type=str,
        help="Video File")
    parser.add_argument("-d","--dir", required=True, type=str,
        help="Directory for saving images")
    args = parser.parse_args()
    img_frm_video(args.file,args.dir)
    