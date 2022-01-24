#!/usr/bin/env python
from sys import exit 
from argparse import ArgumentParser
from cv2 import VideoCapture, imwrite, CAP_PROP_FRAME_COUNT
from os import mkdir
from os.path import join, isdir
from dataclasses import dataclass
from tqdm import tqdm

@dataclass
class ImgFrmVid:
    video_name: str
    save_dir: str

    def img_frm_video (self):
        cap = VideoCapture(self.video_name)
        if not isdir(self.save_dir):
            mkdir(self.save_dir)
        frame_count = int(cap.get(CAP_PROP_FRAME_COUNT))
        if frame_count == 0:
            exit("Video file not found")
        for i in tqdm(range(frame_count), desc ="Extracting"):
            ret, img = cap.read()
            if ret:
                imwrite(join(self.save_dir,'image%d.jpg' %i), img)
        cap.release()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f","--file", required=True, type=str,
    	help="Video File")
    parser.add_argument("-d","--dir", default="images", type=str,
        help="Directory for saving images")
    args = parser.parse_args()
    writer = ImgFrmVid(args.file,args.dir)
    writer.img_frm_video()
    