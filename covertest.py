#!/usr/bin/env python3

import funcs
import sys

file = sys.argv[1]
coverpage = funcs.has_fsul_coverpage(file)

if coverpage:
    print("{0} has a coverpage".format(file)) 
else:
    print("{0} has no coverpage".format(file)) 
