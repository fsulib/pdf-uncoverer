#!/usr/bin/env python3

import pdfuncoverer
import sys

file = sys.argv[1]
coverpage = pdfuncoverer.dump_coverpage_metadata(file)
print(coverpage)
