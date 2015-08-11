#!/usr/bin/python

from __future__ import print_function
import sys
import os

indentsize = int(sys.argv[1].split('=')[1])

line = sys.stdin.readline()
indent = 0
nextindent = 0
last_line = None
in_code_block = False
block_indent = 0
next_block_indent = 0
while line:
  line = line.strip()
  prefix = ''
  if not in_code_block:
    comment_pos = line.find('--')
    if comment_pos >= 0:
      pc = line[:comment_pos]
      comments = line[comment_pos:]
    else:
      pc = line
      comments = ''
    if '[[' in pc:
      codeblock_pos = pc.find('[[')
      pc = pc[:codeblock_pos]
      comments = pc[codeblock_pos:]
      in_code_block = True
      block_indent = 0
      next_block_indent = 1
  if in_code_block:
    if ']]' in line:
      codeblock_end = line.find(']]') + 2
      prefix = line[:codeblock_end]
      pc = line[codeblock_end:]
      in_code_block = False
      comments = ''
    else:
      pc = ''
      comments = line
      if(comments.startswith('if') or comments.startswith('for ') or comments.startswith('while') or comments.startswith('function')
          or comments.startswith('local function') or comments.find(' = function(') >= 0):
        next_block_indent += 1
      elif comments.startswith('elseif') or comments.startswith('else'):
        block_indent -= 1
      if comments.startswith('end') or comments.endswith('end'):
        block_indent -= 1
      indent += block_indent
      block_indent = next_block_indent
  pcs = pc.strip()
  if(pcs.startswith('if') or pcs.startswith('for ') or pcs.startswith('while') or pcs.startswith('function')
      or pcs.startswith('local function') or pcs.find(' = function(') >= 0):
    nextindent += 1
  elif pcs.startswith('elseif') or pcs.startswith('else'):
    indent -= 1
  if pcs.startswith('end') or pcs.endswith('end'):
    indent -= 1
    nextindent -= 1
  # handle brackets...
  excess_brackets = pc.count('(') + pc.count('{') - pc.count(')') - pc.count('}')
  nextindent += excess_brackets
  if excess_brackets < 0 and (pc[0] == ')' or pc[0] == '}'):
    indent = nextindent
  sys.stdout.write(' ' * (indentsize * indent) + prefix + pc + comments + '\n')
  indent = nextindent
  last_line = line
  line = sys.stdin.readline()
if last_line != '':
  sys.stdout.write('\n')

