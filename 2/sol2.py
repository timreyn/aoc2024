import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

def isvalid(vals):
  incr = vals[1] > vals[0]
  for v1, v2 in zip(vals[1:], vals[:-1]):
    if (v1 > v2) != incr or v1 == v2 or abs(v1 - v2) > 3:
      return False
  return True

for line in open(fname):
  line = line.strip()
  vals = [int(x) for x in line.split(' ')]
  if isvalid(vals):
    out += 1
  else:
    for idx in range(len(vals)):
      vals2 = [vals[i] for i in range(len(vals)) if i != idx]
      if isvalid(vals2):
        out += 1
        break

print(out)
