import os

def directory(path):
	for file in os.listdir(path):

		full_path = os.path.join(path,file)
		if not os.path.isdir(full_path):
			print('File:',full_path)
		else:
			print('Directory:',full_path)
			directory(full_path)
directory('/Users/rahjadha/Documents/2020/practice/Python/Crash_Course')