#!/usr/bin/python

from __future__ import print_function
import sys
import os

indentsize = int(sys.argv[1].split('=')[1])

line = sys.stdin.readline()
indent = 0
nextindent = 0
while line:
  line = line.strip()
  if line.startswith('if') or line.startswith('for') or line.startswith('while') or line.startswith('function'):
    nextindent += 1
  elif line.startswith('elseif'):
    indent -= 1
  elif line.startswith('end'):
    indent -= 1
    nextindent -= 1
  sys.stdout.write(' ' * (indentsize * indent) + line + '\n')
  indent = nextindent
  line = sys.stdin.readline()
