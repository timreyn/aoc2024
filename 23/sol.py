import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
all_computers = set()
connections = set()

for line in open(fname):
  line = line.strip().split('-')
  l = sorted([line[0], line[1]])
  all_computers.add(l[0])
  all_computers.add(l[1])
  connections.add((l[0], l[1]))

for c1 in all_computers:
  for c2 in all_computers:
    if (c1, c2) not in connections:
      continue
    for c3 in all_computers:
      if (c1, c3) in connections and (c2, c3) in connections and (c1.startswith('t') or c2.startswith('t') or c3.startswith('t')):
        out += 1
        print(c1, c2, c3)


print(out)
