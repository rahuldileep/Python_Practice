#!/usr/bin/env python3

import re

def rearrange(name):
	result = re.search(r"^([\w .]*), ([\w .]*)$",name)
	if result == None:
		return name
	return "{} {}".format(result.groups()[1], result.groups()[0])

print(rearrange("Jadhav, Rahul D."))