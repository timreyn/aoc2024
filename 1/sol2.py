import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
left = []
right = []

for line in open(fname):
  line = line.strip().split()
  left += [int(line[0])]
  right += [int(line[1])]

for x in left:
  for y in right:
    if x == y:
      out += y

print(out)
