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
  comment_pos = line.find('--')
  if comment_pos >= 0:
    pc = line[:comment_pos]
    comments = line[comment_pos:]
  else:
    pc = line
    comments = ''
  if(pc.startswith('if') or pc.startswith('for ') or pc.startswith('while') or pc.startswith('function')
      or pc.startswith('local function') or pc.find(' = function(') >= 0):
    nextindent += 1
  elif pc.startswith('elseif') or pc.startswith('else'):
    indent -= 1
  if pc.startswith('end') or pc.endswith('end'):
    indent -= 1
    nextindent -= 1
  # handle brackets...
  excess_brackets = pc.count('(') + pc.count('{') - pc.count(')') - pc.count('}')
  nextindent += excess_brackets
  if excess_brackets < 0 and (pc[0] == ')' or pc[0] == '}'):
    indent = nextindent
  sys.stdout.write(' ' * (indentsize * indent) + pc + comments + '\n')
  indent = nextindent
  last_line = line
  line = sys.stdin.readline()
if last_line != '':
  sys.stdout.write('\n')

