import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
grid = []
queue = []
EAST = (0,1)
SOUTH = (1,0)
NORTH = (-1,0)
WEST = (0,-1)


def p(a,b):
  return (a[0]+b[0], a[1]+b[1])
def g(grid, p):
  return grid[p[0]][p[1]]
def rotations(d):
  return ((d[1], d[0]), (d[1] * -1, d[0] * -1))

def add_candidate(queue, pos, d, score):
  for i in range(len(queue)):
    if queue[i][2] > score:
      queue.insert(i, (pos, d, score))
      return
  queue.insert(len(queue), (pos, d, score))

for line in open(fname):
  line = line.strip()
  if 'S' in line:
    start = (len(grid), line.index('S'))
  grid += [line]

queue += [(start, EAST, 0)]
done = set()

while queue:
  pos, d, score = queue.pop(0)
  if g(grid, pos) == 'E':
    print(score)
    break
  if (pos, d) in done:
    continue
  if g(grid, pos) == '#':
    continue
  done.add((pos, d))
  add_candidate(queue, p(pos, d), d, score + 1)
  for dd in rotations(d):
    add_candidate(queue, pos, dd, score + 1000)
