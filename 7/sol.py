import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

def is_valid(vals, target):
  if len(vals) == 1:
    return vals[0] == target
  return is_valid([vals[0] * vals[1]] + vals[2:], target) or is_valid([vals[0] + vals[1]] + vals[2:], target)

for line in open(fname):
  line = line.strip()
  target = int(line.split(':')[0])
  vals = [int(x) for x in line.split(' ')[1:]]
  if is_valid(vals, target):
    out += target


print(out)
