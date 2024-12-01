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

left.sort()
right.sort()

for x,y in zip(left, right):
  out += abs(x - y)


print(out)
