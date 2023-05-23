#!/usr/bin/env python3

import sys
import os
import subprocess
from multiprocessing import Pool

def backup_func(tree_top, bakdir_name):
    top_dir = os.path.basename(tree_top)
    tree_top += os.sep
    for dir, subdirs, files in os.walk(tree_top):
        re_path = dir.replace(tree_top,'')
        backup_dir = os.path.join(bakdir_name, re_path)
        os.makedirs(backup_dir)
        for f in files:
            filepath = os.path.join(dir, f)
            destpath = os.path.join(backup_dir, f)
            subprocess.run(['rsync','-zvh',filepath,destpath])



source = '/Users/rahjadha/Documents/2020/practice'
dest   = '/Users/rahjadha/Documents/2020/backup_practice'
backup_func(source,dest)