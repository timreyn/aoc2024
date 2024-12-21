import collections
import itertools
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['X', '0', 'A']]
directional = [['X', '^', 'A'], ['<', 'v', '>']]

dirs = {
  '^': (-1, 0),
  'v': (1, 0),
  '<': (0, -1),
  '>': (0, 1),
}

def times(k, d):
  return (d[0] * k, d[1] * k)

def plus(a, b):
  return (a[0] + b[0], a[1] + b[1])

def is_valid(a, b, seq, grid):
  for d in seq[:-1]:
    a = (a[0] + dirs[d][0], a[1] + dirs[d][1])
    if grid[a[0]][a[1]] == 'X':
      return False
  return True

def options_from(a, b, grid):
  xa = -1
  xb = -1
  ya = -1
  yb = -1
  for x, row in enumerate(grid):
    for y, v in enumerate(row):
      if v == a:
        xa = x
        ya = y
      if v == b:
        xb = x
        yb = y
  out = []
  horiz_component = []
  vert_component = []
  if xa < xb:
    horiz_component = ['v'] * (xb - xa)
  if xa > xb:
    horiz_component = ['^'] * (xa - xb)
  if ya > yb:
    vert_component = ['<'] * (ya - yb)
  if ya < yb:
    vert_component = ['>'] * (yb - ya)
  if horiz_component and vert_component:
    out = [horiz_component + vert_component + ['A'], vert_component + horiz_component + ['A']]
  elif horiz_component:
    out = [horiz_component + ['A']]
  elif vert_component:
    out = [vert_component + ['A']]
  else:
    out = [['A']]
  out = [x for x in out if is_valid((xa, ya), (xb, yb), x, grid)]
  return out

def translate(seq, grid):
  xa = -1
  ya = -1
  out = []
  for x, row in enumerate(grid):
    for y, v in enumerate(row):
      if v == 'A':
        xa = x
        ya = y
  for d in seq:
    if d == 'A':
      out += [grid[xa][ya]]
    else:
      (xa, ya) = (xa + dirs[d][0], ya + dirs[d][1])
  return out

'''
s = translate('<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A', directional)
print(s)
s = translate(s, directional)
print(s)
'''

for line in open(fname):
  line = line.strip()
  cur = 'A'
  options = [[]]
  for x in line:
    options = [o1 + o2 for o1, o2 in itertools.product(options, options_from(cur, x, keypad))]
    cur = x
  options2 = []
  for o in options:
    cur = 'A'
    suboptions = [[]]
    for x in o:
      suboptions = [o1 + o2 for o1, o2 in itertools.product(suboptions, options_from(cur, x, directional))]
      cur = x
    options2 += suboptions
  options3 = []
  for o in options2:
    cur = 'A'
    suboptions = [[]]
    for x in o:
      suboptions = [o1 + o2 for o1, o2 in itertools.product(suboptions, options_from(cur, x, directional))]
      cur = x
    options3 += suboptions
  l = min([len(x) for x in options3])
  out += int(line[:-1]) * l




print(out)
