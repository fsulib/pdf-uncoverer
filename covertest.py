#!/usr/bin/env python3

import sys
from pypdf import PdfReader

file = sys.argv[1]
reader = PdfReader(file)

coverpage = False
page1 = reader.pages[0]
if '/Annots' in page1:
    for annot in page1['/Annots']:
        if annot.get_object()['/A']['/URI'] == 'mailto:lib-ir@fsu.edu':
            coverpage = True

if coverpage:
    print("{0} has a coverpage".format(file)) 
else:
    print("{0} has no coverpage".format(file)) 



