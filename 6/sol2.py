import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
grid = []

x = -1
y = -1
ds = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
d = None

for line in open(fname):
  line = line.strip()
  for c in ds.keys():
    if c in line:
      x = len(grid)
      y = line.index(c)
      d = ds[c]
  grid += [line]

def does_it_loop(x, y, d, grid):
  visited = set()

  while True:
    if ((x, y, d) in visited):
      return True
    visited.add((x, y, d))
    xx = x + d[0]
    yy = y + d[1]
    if xx < 0 or xx >= len(grid) or yy < 0 or yy >= len(grid[x]):
      return False
    if grid[xx][yy] == '#':
      d = (d[1], -1 * d[0])
    else:
      x = xx
      y = yy

for i in range(len(grid)):
  for j in range(len(grid[i])):
    gg = [[l for l in k] for k in grid]
    if gg[i][j] != '.':
      continue
    gg[i][j] = '#'
    if does_it_loop(x, y, d, gg):
      out += 1

print(out)
