import collections
import numpy as np
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
current = []

for line in open(fname):
  line = line.strip()
  if not line:
    continue
  l = line.split(':')[1]
  vals = l.split(', ')
  if len(current) == 0 or len(current) == 1:
    current += [[int(val.split('+')[1]) for val in vals]]
  else:
    vv = [int(val.split('=')[1]) for val in vals]
    a = np.array(current)
    b = np.array(vv)
    x = np.linalg.solve(np.transpose(a), b).tolist()
    if x[0] > 0 and x[1] > 0:
      print(x)
      aa = round(x[0])
      bb = round(x[1])
      if abs(aa - x[0]) < 1e-6 and abs(bb - x[1]) < 1e-6:
        out += aa * 3 + bb
    else:
      print('invalid')
    current = []


print(out)
