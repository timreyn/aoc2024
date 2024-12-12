import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

grid = []
total = 0

for line in open(fname):
  line = line.strip()
  grid += [line]
  total += len(line)

used = set()

while len(used) < total:
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if (i,j) not in used:
        current_region = set()
        borders = 0
        queue = [(i,j)]
        while queue:
          n = queue.pop()
          current_region.add(n)
          ii = n[0]
          jj = n[1]
          for d in [(0,1), (1,0), (-1,0), (0,-1)]:
            iii = ii + d[0]
            jjj = jj + d[1]
            if iii < 0 or iii >= len(grid) or jjj < 0 or jjj >= len(grid[iii]) or grid[iii][jjj] != grid[i][j]:
              borders += 1
            elif (iii, jjj) not in queue and (iii, jjj) not in current_region:
              queue += [(iii, jjj)]
        out += len(current_region) * borders
        for n in current_region:
          used.add(n)



print(out)
