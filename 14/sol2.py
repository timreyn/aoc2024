import collections
import sys
import re

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
dx = 101 if len(sys.argv) < 3 else int(sys.argv[2])
dy = 103 if len(sys.argv) < 4 else int(sys.argv[3])

out = 0
quadrants = collections.defaultdict(int)
vals = []

for line in open(fname):
  line = line.strip()
  m = re.match(r'p=(\d*),(\d*) v=(-?\d*),(-?\d*)', line)
  x = int(m.group(1))
  y = int(m.group(2))
  vx = int(m.group(3))
  vy = int(m.group(4))
  vals += [(x, y, vx, vy)]

steps = 0
# it loops every 103 * 101
while steps < 10403:
  steps += 1
  vals = [((x + vx) % dx, (y + vy) % dy, vx, vy) for (x, y, vx, vy) in vals]
  pts = [(x, y) for (x, y, vx, vy) in vals]

  # idk, from messing around it seems like shapes form on a cycle.
  if steps % 101 != 2444 % 101:
    continue
  print(steps)
  for i in range(dy):
    line = ''
    for j in range(dx):
      if (j, i) in pts:
        line += '#'
      else:
        line += '.'
    print(line)
  print()
  print()
  print()
