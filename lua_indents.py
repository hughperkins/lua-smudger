#!/usr/bin/python

from __future__ import print_function
import sys
import os

indentsize = int(sys.argv[1].split('=')[1])

line = sys.stdin.readline()
indent = 0
nextindent = 0
last_line = None
while line:
  line = line.strip()
  if(line.startswith('if') or line.startswith('for') or line.startswith('while') or line.startswith('function')
      or line.startswith('local function')):
    nextindent += 1
  elif line.startswith('elseif') or line.startswith('else'):
    indent -= 1
  elif line.startswith('end'):
    indent -= 1
    nextindent -= 1
  # handle brackets...
  nextindent += line.count('(') - line.count(')')
  sys.stdout.write(' ' * (indentsize * indent) + line + '\n')
  indent = nextindent
  last_line = line
  line = sys.stdin.readline()
if last_line != '':
  sys.stdout.write('\n')

