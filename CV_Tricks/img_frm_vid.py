#!/usr/bin/env python
import sys, argparse
import cv2
from os import mkdir, path
from dataclasses import dataclass
from tqdm import tqdm

@dataclass
class ImgFrmVid:
    video_name: str
    save_dir: str

    def img_frm_video (self):
        cap = cv2.VideoCapture(self.video_name)
        print('Reading video file')
        if not path.isdir(self.save_dir):
            mkdir(self.save_dir)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if frame_count == 0:
            sys.exit("Unable to read the video file")
        for i in tqdm(range(frame_count), desc ="Extracted Frames"):
            ret, img = cap.read()
            if ret:
                cv2.imwrite(path.join(self.save_dir,'image%d.jpg' %i), img)
        print("Done")
        cap.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", required=True, type=str,
    	help="Video File")
    parser.add_argument("-d","--dir", required=True, type=str,
        help="Directory for saving images")
    args = parser.parse_args()
    writer = ImgFrmVid(args.file,args.dir)
    writer.img_frm_video()
    