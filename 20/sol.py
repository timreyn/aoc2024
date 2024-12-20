import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
grid = []
start = None
end = None

for line in open(fname):
  line = line.strip()
  if 'S' in line:
    start = (len(grid), line.index('S'))
  if 'E' in line:
    end = (len(grid), line.index('E'))
  grid += [line]

def compute_optimal(grid, target):
  optimal = {}
  queue = [(target, 0)]
  while queue:
    pos, dis = queue.pop(0)
    optimal[pos] = dis
    for d in [(0,1), (1,0), (0,-1), (-1,0)]:
      nn = (pos[0] + d[0], pos[1] + d[1])
      if nn in optimal:
        continue
      if nn[0] < 0 or nn[0] >= len(grid) or nn[1] < 0 or nn[1] >= len(grid[0]):
        continue
      if grid[nn[0]][nn[1]] != '#':
        queue += [(nn, dis + 1)]
  return optimal

optimal_end = compute_optimal(grid, end)
optimal_start = compute_optimal(grid, start)

best = optimal_start[end]
print(best)

for x in range(len(grid)):
  for y in range(len(grid[x])):
    if grid[x][y] != '#':
      continue
    for d1 in [(0,1), (1,0), (0,-1), (-1,0)]:
      for d2 in [(0,1), (1,0), (0,-1), (-1,0)]:
        p1 = (x + d1[0], y + d1[1])
        p2 = (x + d2[0], y + d2[1])
        if p1 in optimal_start and p2 in optimal_end:
          d = optimal_start[p1] + optimal_end[p2] + 2
          if best - d >= 100:
            out += 1


print(out)
