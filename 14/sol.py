import collections
import sys
import re

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
dx = 101 if len(sys.argv) < 3 else int(sys.argv[2])
dy = 103 if len(sys.argv) < 4 else int(sys.argv[3])

out = 0
quadrants = collections.defaultdict(int)

for line in open(fname):
  line = line.strip()
  m = re.match(r'p=(\d*),(\d*) v=(-?\d*),(-?\d*)', line)
  x = int(m.group(1))
  y = int(m.group(2))
  vx = int(m.group(3))
  vy = int(m.group(4))

  x_final = (x + vx * 100) % dx
  y_final = (y + vy * 100) % dy

  print(x_final, y_final)
  if x_final == dx // 2 or y_final == dy // 2:
    continue
  quadrants[(x_final < dx // 2, y_final < dy // 2)] += 1

out = 1
for k,v in quadrants.items():
  out *= v
print(out)
