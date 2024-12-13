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
    b = np.array(vv) + np.array([10000000000000, 10000000000000])
    x = np.linalg.solve(np.transpose(a), b).tolist()
    if x[0] > 0 and x[1] > 0:
      print(x)
      aa = round(x[0])
      bb = round(x[1])
      sol = np.array([aa, bb])
      if np.array_equal(np.matmul(np.transpose(a), sol), b):
        out += aa * 3 + bb
      else:
        print('mismatch')
        print(np.matmul(np.transpose(a), sol))
        print(b)
    else:
      print('invalid')
    current = []


print(out)
