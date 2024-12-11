import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
vals = collections.defaultdict(int)

for line in open(fname):
  for x in line.strip().split(' '):
    vals[int(x)] += 1

for i in range(75):
  print(i, len(vals))
  nextvals = collections.defaultdict(int)
  for v, ct in vals.items():
    if v == 0:
      nextvals[1] += ct
    elif len(str(v)) % 2 == 0:
      vv = str(v)
      nextvals[int(vv[0:len(vv)//2])] += ct
      nextvals[int(vv[len(vv)//2:])] += ct
    else:
      nextvals[v * 2024] += ct
  vals = nextvals

for x, ct in vals.items():
  out += ct
print(out)
