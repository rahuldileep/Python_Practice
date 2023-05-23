#!/usr/bin/env python3

import psutil
import shutil
from network import *

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def check_cpu_percent(disk):
	usage = shutil.cpu_percent()
	return usage < 75

if not check_disk_usage('/') and not check_cpu_percent():
	print("Error! Disk/CPU usage warning")

elif check_localhost() and check_connectivity():
	print("Everything is ok")

else:
	print("Network Checks Failed")