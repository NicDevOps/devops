import glob
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

list_of_files = sorted(glob.glob('ascii_files/*.txt'))
latest_file = list_of_files[-1]
f = open(latest_file, 'r')

print(f.read())
