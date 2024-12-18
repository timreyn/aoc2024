import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
size = 70 if len(sys.argv) < 3 else int(sys.argv[2])
to_use = 1024 if len(sys.argv) < 4 else int(sys.argv[3])

out = 0
coords = []

for line in open(fname):
  line = line.strip()
  coords += [tuple(int(x) for x in line.split(','))]
  if len(coords) == to_use:
    break

visited = set()
queue = [(0, 0, 0)]

while queue:
  x, y, d = queue.pop(0)
  if x == size and y == size:
    print(d)
    break
  if (x, y) in visited:
    continue
  visited.add((x,y))
  for n in [(0,1), (1,0), (0,-1), (-1,0)]:
    xx = x + n[0]
    yy = y + n[1]
    if xx >= 0 and xx <= size and yy >= 0 and yy <= size and (xx, yy) not in visited and (xx, yy) not in coords:
      queue += [(xx, yy, d + 1)]
