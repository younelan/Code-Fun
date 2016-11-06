#!/usr/bin/env python2.7
import os
from os.path import join, getsize

DIR_NAME="/etc/"

for root, dirs, files in os.walk(DIR_NAME):
    print "%35s: %6iK in %4i files" %(
      root, 
      int(sum(getsize(join(root, name)) for name in files)/1024),
       len(files), 
    )
    if '.git' in dirs:
        dirs.remove('.git')
