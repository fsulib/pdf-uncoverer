#!/usr/bin/env python3

import funcs
import sys
import os
import shutil

folder = sys.argv[1]
if not os.path.exists(folder):
  sys.exit("{} does not exist.".format(folder))
if not os.path.isdir(folder):
  sys.exit("{} is not a folder.".format(folder))

procfolder = "{}_processed".format(folder)
if os.path.exists(procfolder):
  shutil.rmtree(procfolder)
os.makedirs(procfolder) 

for file in os.listdir(folder):
  if file.endswith(".pdf"):
    if funcs.has_fsul_coverpage("{}/{}".format(folder, file)):
      print("{} DOES have FSUL coverpage".format(file))
    else:
      print("{} DOES NOT have FSUL coverpage".format(file))
