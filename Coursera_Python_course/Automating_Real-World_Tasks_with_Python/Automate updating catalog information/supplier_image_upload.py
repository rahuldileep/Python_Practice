#!/usr/bin/env python3

import glob
import os
import requests

dir = os.path.dirname(os.path.abspath(__file__))
src = dir +'/supplier-data/images/'+ '*.jpeg'

for infile in glob.glob(src):
  with open(infile, 'rb') as fp:
    requests.post("http://localhost/upload/", files = {'file': fp})