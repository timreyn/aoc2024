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

def add_candidate(queue, pos, d, score, path):
  for i in range(len(queue)):
    if queue[i][2] > score:
      queue.insert(i, (pos, d, score, path))
      return
  queue.insert(len(queue), (pos, d, score, path))

for line in open(fname):
  line = line.strip()
  if 'S' in line:
    start = (len(grid), line.index('S'))
  grid += [line]

queue += [(start, EAST, 0, [start])]
done = {}
best_score = -1
bests = []
cur_score = 0

while queue:
  pos, d, score, path = queue.pop(0)
  if score > cur_score:
    cur_score = score
    if cur_score % 100 == 0:
      print(cur_score)
  if g(grid, pos) == 'E':
    if score > best_score and best_score > -1:
      break
    bests += path
    best_score = score
    continue
  if best_score > -1 and score > best_score:
    break
  if (pos, d) in done and done[(pos, d)] < score:
    continue
  if g(grid, pos) == '#':
    continue
  done[(pos, d)] = score
  add_candidate(queue, p(pos, d), d, score + 1, path + [p(pos, d)])
  for dd in rotations(d):
    add_candidate(queue, pos, dd, score + 1000, path)

print(len(set(bests)))
