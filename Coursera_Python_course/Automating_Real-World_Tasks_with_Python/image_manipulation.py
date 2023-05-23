#!/usr/bin/env python3
from PIL import Image
import os
import sys

image_dir = sys.argv[1]
dest_dir = sys.argv[2]

for image in os.listdir(image_dir):
    img_path = os.path.join(image_dir,image)
    dest_path = os.path.join(dest_dir,image)
    im = Image.open(img_path)
    new_im = im.rotate(90).resize((128,128)).convert('RGB')
    new_im.save(dest_path,'jpeg')           