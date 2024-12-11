import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
vals = []

for line in open(fname):
  vals = [int(x) for x in line.strip().split(' ')]

for i in range(25):
  nextvals = []
  for v in vals:
    if v == 0:
      nextvals += [1]
    elif len(str(v)) % 2 == 0:
      vv = str(v)
      nextvals += [int(vv[0:len(vv)//2]), int(vv[len(vv)//2:])]
    else:
      nextvals += [v * 2024]
  vals = nextvals

print(len(vals))
