import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

grid = []

def get(grid, i, j):
  if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
    return ''
  return grid[i][j]

for line in open(fname):
  line = line.strip()
  grid += [line]

for i in range(len(grid)):
  for j in range(len(grid[i])):
    if get(grid, i, j) != 'A':
      continue
    if (set([get(grid, i + 1, j + 1), get(grid, i - 1, j - 1)]) == set(['M', 'S']) and
        set([get(grid, i + 1, j - 1), get(grid, i - 1, j + 1)]) == set(['M', 'S'])):
      out += 1

print(out)
