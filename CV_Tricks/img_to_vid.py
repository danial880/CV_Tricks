#!usr/bin/env python
from sys import exit
from argparse import ArgumentParser
from os import listdir
from os.path import isfile, join
from cv2 import imread, VideoWriter_fourcc, VideoWriter, resize
from re import compile
from dataclasses import dataclass
from tqdm import tqdm

@dataclass
class ImgToVid:
	img_dir: str
	name: str
	extension: str
	fps: str
	size: tuple

	def sort_files(self, value):
		num = compile(r'(\d+)')
		chunks = num.split(value)
		chunks[1::2] = map(int, chunks[1::2])
		return chunks

	def img_to_video(self):
	    codec = VideoWriter_fourcc(*'XVID')
	    video_name = self.name + "." + self.extension
	    writer = VideoWriter(video_name, codec, self.fps, self.size)
	    try:
	    	files = [file for file in listdir(self.img_dir) 
	    			if isfile(join(self.img_dir, file))]
	    except Exception as e :
	    	exit(e)
	    files.sort(key = self.sort_files)
	    if len(files) == 0:
	    	exit("{} not found!!!".format(self.img_dir))
	    for i in tqdm(range(len(files)), desc ="Making"):
	        filename = self.img_dir + "/" + files[i]
	        img = imread(filename)
	        img = resize(img, self.size)
	        writer.write(img)
	    writer.release()
 
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f","--file", required=True, type=str,
    	help="Image directory")
    parser.add_argument("-n","--name", default="result", type=str,
        help="Name of the new video created from images")
    parser.add_argument("-e","--extension", default="avi", type=str,
    	help="Video file saving format e.g. avi, mp4")
    parser.add_argument("--fps", default=25, type=str,
    	help="Frame rate")
    parser.add_argument("-s","--size", default=(640,480), type=str,
    	help="Custom frame size of video")
    args = parser.parse_args()
    writer = ImgToVid(args.file, args.name, args.extension, args.fps, args.size)
    writer.img_to_video()
