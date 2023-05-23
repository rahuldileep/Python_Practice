#!/usr/bin/env python3
import sys
import os


filename = sys.argv[1]

if not os.path.exists(filename):
	with open(filename, "w") as file:
		file.write("New file created")
else:
	print("Error: The file {} already exists".format(filename))
	sys.exit(1)