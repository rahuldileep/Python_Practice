#!/usr/bin/env python3

import os
import glob
from PIL import Image

dir = os.path.dirname(os.path.abspath(__file__))
img_dir = dir +'/supplier-data/images/'+ '*.tiff'

for infile in glob.glob(img_dir):
  file, ext = os.path.splitext(infile)
  im = Image.open(infile)
  im.convert('RGB')
  im = im.resize((600,400))
  im.save(file+'.jpeg','JPEG')