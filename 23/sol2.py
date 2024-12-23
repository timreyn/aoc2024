import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

all_computers = set()
connections = set()

for line in open(fname):
  line = line.strip().split('-')
  l = sorted([line[0], line[1]])
  all_computers.add(l[0])
  all_computers.add(l[1])
  connections.add((l[0], l[1]))

candidates = connections

while len(candidates) > 1:
  print(len(candidates))
  new_candidates = []
  for cand in candidates:
    for c in all_computers:
      valid = True
      for cc in cand:
        if (c, cc) not in connections:
          valid = False
      if valid:
        new_candidates += [list(cand) + [c]]
  candidates = new_candidates

print(','.join(sorted(candidates[0])))
