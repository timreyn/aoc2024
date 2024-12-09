import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

arr = []

for line in open(fname):
  line = line.strip()
  active = True
  current_id = 0
  for c in line:
    if active:
      arr += [current_id] * int(c)
      current_id += 1
    else:
      arr += ['.'] * int(c)
    active = not active
while '.' in arr:
  arr[arr.index('.')] = arr[-1]
  arr.pop()

for idx, value in enumerate(arr):
  out += idx * value

print(out)
