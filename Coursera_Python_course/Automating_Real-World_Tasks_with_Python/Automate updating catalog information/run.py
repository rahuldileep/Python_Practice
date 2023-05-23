#!/usr/bin/env python3

import os
import json
import requests

dir = os.path.dirname(os.path.abspath(__file__))
src = dir +'/supplier-data/descriptions'
l = []
for infile in os.listdir(src):
  d = dict()
  file, ext = os.path.splitext(infile)
  file_path = os.path.join(src,infile)
  with open(file_path) as fp:
    reader = fp.read().strip().splitlines()
    d["name"] = reader[0]
    d["weight"] = int(reader[1].rstrip("lbs"))
    d["description"] = reader[2]
    d["image_name"] = file+".jpeg" 
  d = json.dumps(d)
  r = requests.post("http://35.226.144.139/fruits",data = d)
  print(d)