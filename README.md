# CV_Tricks [![GitHub license](https://img.shields.io/github/license/danial880/CV_Tricks?style=plastic)](https://github.com/danial880/CV_Tricks/blob/main/LICENSE) [![PyPI](https://img.shields.io/pypi/v/CV-Tricks?style=plastic)](https://pypi.org/project/CV-Tricks/) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/CV-Tricks?style=plastic)

### CLI commands for making videos into images and vice versa.

#### Images from Video

```
Usage:
	img_frm_vid.py [-f][--file] [-d][--dir]

Required:
	[-f][--file]	input video file

Options:
	[-d][--dir]	path to output folder. Default is "images". Directory will be created if not exist.

Examples:
	
	img_frm_vid.py -f video.py
or
	img_frm_vid.py --file video.py --dir saved_images
```

#### Images to Video

```
Usage:
	img_to_vid.py [-f][--file] [-n][--name] [-e][--extension] [--fps] [-s][--size]


Required:
	[-f][--file]	input image directory

Options:
	[-n][--name]	name of video created. Default is "result".
	[-e][--extension] video file saving format. Default is "avi".
	[--fps] frame per second. Default is 25.
	[-s][--size] frame size of video. Default is (640,480)
	

Examples:
	
	img_to_vid.py -f images_directory
or
	img_to_vid.py --file video.py --size 1080 720
```

> **_NOTE:_**  This repository is under active development. New features coming soon!!!