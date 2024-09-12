#!/usr/bin/env python3

import pdfuncoverer
import sys

file = sys.argv[1]
coverpage = pdfuncoverer.has_coverpage(file)

if coverpage:
    print("{0} has a coverpage".format(file)) 
else:
    print("{0} has no coverpage".format(file)) 



