#!/usr/bin/env python3

import funcs
import sys
import os

file = sys.argv[1]
if not os.path.exists(file):
  sys.exit("{} does not exist.".format(file))
if not os.path.isfile(file):
  sys.exit("{} is not a file.".format(file))

coverpage = funcs.has_fsul_coverpage(file)
if coverpage:
    print("{0} has a coverpage".format(file)) 
else:
    print("{0} has no coverpage".format(file)) 
