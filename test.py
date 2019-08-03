import os
import shutil
import subprocess as bash

def get_this_folder():
    return os.path.dirname(os.path.realpath(__file__))

dest = os.path.expanduser('~/user')
print(dest)
shutil.copy(get_this_folder()+'/README.md',dest)
