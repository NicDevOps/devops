import glob
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

list_of_files = glob.glob('ascii_files/*.txt')
latest_file = max(list_of_files, key=os.path.getctime)
f = open(latest_file, 'r')

print(f.read())
