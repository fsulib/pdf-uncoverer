#!/usr/bin/env python3

import funcs
import sys
import os
import shutil
import subprocess

folder = sys.argv[1]
if not os.path.exists(folder):
  sys.exit('{} does not exist.'.format(folder))
if not os.path.isdir(folder):
  sys.exit('{} is not a folder.'.format(folder))

procfolder = '{}_processed'.format(folder)
if os.path.exists(procfolder):
  shutil.rmtree(procfolder)
os.makedirs(procfolder) 

counts = {'total': 0, 'uncovered': 0, 'decovered': 0}

for file in os.listdir(folder):
  counts['total'] += 1
  print('')
  if file.endswith('.pdf'):
    if not funcs.has_fsul_coverpage('{}/{}'.format(folder, file)):
      counts['uncovered'] += 1
      print('{} does not have an FSUL coverpage.'.format(file))
    else:
      counts['decovered'] += 1
      print('{} has an FSUL coverpage.'.format(file))
      subprocess.run(['pdftk', '{}/{}'.format(folder, file), 'cat', '2-end', 'output', '{}/{}'.format(procfolder, file)]) 
      print('{} has has been copied to {} without coverpage.'.format(file, procfolder))

print('')
print('Total PDFs in {}: {}'.format(folder, counts['total']))
print('Total PDFs skipped due to lack of FSUL coverpage: {}'.format(counts['uncovered']))
print('Total PDFs processed into {} to remove FSUL coverpage: {}'.format(procfolder, counts['decovered']))
