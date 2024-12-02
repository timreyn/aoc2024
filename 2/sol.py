import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

for line in open(fname):
  line = line.strip()
  vals = [int(x) for x in line.split(' ')]
  incr = vals[1] > vals[0]
  valid = True
  for v1, v2 in zip(vals[1:], vals[:-1]):
    if (v1 > v2) != incr or v1 == v2 or abs(v1 - v2) > 3:
      valid = False
      break
  if valid:
    out += 1

print(out)
