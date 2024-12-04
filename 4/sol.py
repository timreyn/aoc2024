import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

grid = []

dirs = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

for line in open(fname):
  line = line.strip()
  grid += [line]

for i in range(len(grid)):
  for j in range(len(grid[i])):
    for d in dirs:
      works = True
      for amt, ltr in enumerate('XMAS'):
        ii = i + amt * d[0]
        jj = j + amt * d[1]
        if not (ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[ii]) and grid[ii][jj] == ltr):
          works = False
      if works:
        out += 1




print(out)
