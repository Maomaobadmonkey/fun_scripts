# system functions and shell utility
import os, shutil
# pass in a path and it gives you all files within path
import glob
# File visualization bar
import tqdm
# system 
import sys

# File Paths
dst = ("C:\\Users\\Iron Nomad\\Desktop\\STL Files")
src = ("C:\\Users\\Iron Nomad\\Desktop")


files = glob.glob(os.path.join(src, "*.gcode"))
# https://docs.python.org/2/library/os.path.html#os.path.splitext
# https://github.com/tqdm/tqdm

if len(files) == 0:
    print('Sorry, nothing to move!')
    sys.exit()

for f in tqdm.tqdm(files):
    root, ext = os.path.splitext(f)
    
    if ext == '.gcode':
        shutil.move(f, dst)
    