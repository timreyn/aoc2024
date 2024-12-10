import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
grid = []

scores = {}

def nbrs(x, y, grid):
  if x > 0:
    yield (x-1, y)
  if y > 0:
    yield (x, y-1)
  if x < len(grid) - 1:
    yield (x+1, y)
  if y < len(grid[x]) - 1:
    yield (x, y+1)

for line in open(fname):
  line = line.strip()
  grid += [line]

for i in [9,8,7,6,5,4,3,2,1,0]:
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      if grid[x][y] != str(i):
        continue
      score = []
      if i == 9:
        score = [(x, y)]
      for xx, yy in nbrs(x, y, grid):
        if grid[xx][yy] == str(i+1):
          score += scores[(xx, yy)]
      scores[(x, y)] = list(set(score))
      if i == 0:
        out += len(set(score))
        print(len(set(score)))


print(out)
