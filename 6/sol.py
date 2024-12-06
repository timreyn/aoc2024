import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
grid = []

x = -1
y = -1
ds = {'^': [-1, 0], 'v': [1, 0], '<': [0, -1], '>': [0, 1]}
d = None

visited = set()

for line in open(fname):
  line = line.strip()
  for c in ds.keys():
    if c in line:
      x = len(grid)
      y = line.index(c)
      d = ds[c]
  grid += [line]

while True:
  visited.add((x, y))
  xx = x + d[0]
  yy = y + d[1]
  if xx < 0 or xx >= len(grid) or yy < 0 or yy >= len(grid[x]):
    break
  if grid[xx][yy] == '#':
    d = [d[1], -1 * d[0]]
  else:
    x = xx
    y = yy

print(len(visited))
