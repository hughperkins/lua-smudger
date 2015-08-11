#!/usr/bin/python

from __future__ import print_function
import sys
import os

indentsize = int(sys.argv[1].split('=')[1])

line = sys.stdin.readline()
indent = 0
nextindent = 0
last_line = None
last_excess_braces = 0
#brace_indentation = 0
while line:
  line = line.strip()
  if(line.startswith('if') or line.startswith('for') or line.startswith('while') or line.startswith('function')
      or line.startswith('local function') or line.find(' = function(') >= 0):
    nextindent += 1
  elif line.startswith('elseif') or line.startswith('else'):
    indent -= 1
  if line.startswith('end') or line.endswith('end'):
    indent -= 1
    nextindent -= 1
  # handle brackets...
  this_excess_braces = line.count('(') - line.count(')')
  nextindent += this_excess_braces
  if last_excess_braces == 0 and this_excess_braces > 0:
    # lets split it out to next line...
    brace_pos = line.find('(')
    line_1 = line[:brace_pos + 1]
    line_2 = line[brace_pos + 1:]
    sys.stdout.write(' ' * (indentsize * indent) + line_1 + '\n')
    line = line_2
    indent += 1
  last_excess_braces = this_excess_braces
#  new_excess_braces = excess_braces + this_excess_braces
#  if excess_braces > 0 or new_excess_braces > 0:
#    print('brace old=', excess_braces, 'new=', new_excess_braces, 'brace_indentation', brace_indentation)
##  if excess_braces > 0:
##    indent += brace_indentation - 1
#  if excess_braces == 0 and new_excess_braces > 0:
#    brace_indentation = (line.find('(') + 1 )
#    print('update brace_indentation to', brace_indentation)
#  if 
#  excess_braces = new_excess_braces
  sys.stdout.write(' ' * (indentsize * indent) + line + '\n')
  indent = nextindent
  last_line = line
  line = sys.stdin.readline()
if last_line != '':
  sys.stdout.write('\n')

