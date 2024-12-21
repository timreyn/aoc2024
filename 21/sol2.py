import collections
import itertools
import sys
import functools

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
max_depth = 25 if len(sys.argv) < 3 else int(sys.argv[2])

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

@functools.cache
def compute_optimal(a, b, depth):
  if depth == max_depth:
    grid = keypad
  else:
    grid = directional
  out = -1
  for o in options_from(a, b, grid):
    if depth == 0:
      return len(o)
    total = 0
    cur = 'A'
    for x in o:
      total += compute_optimal(cur, x, depth - 1)
      cur = x
    if out < 0 or total < out:
      out = total
  return out

for line in open(fname):
  line = line.strip()
  cur = 'A'
  total = 0
  for x in line:
    total += compute_optimal(cur, x, max_depth)
    cur = x
  out += int(line[:-1]) * total

print(out)
