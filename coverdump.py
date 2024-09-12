#!/usr/bin/env python3

import pdfuncoverer
import pprint
import sys

file = sys.argv[1]
coverpage = pdfuncoverer.dump_coverpage_metadata(file)
pprint.pprint(coverpage)
