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
      arr += [(current_id, int(c))]
      current_id += 1
    else:
      arr += [(-1, int(c))]
    active = not active

to_move = max([x[0] for x in arr])
while to_move > 0:
  print(to_move)
  num_to_move = [x for x in arr if x[0] == to_move][0][1]
  for i in range(len(arr)):
    if arr[i][0] == to_move:
      break
    if (arr[i][0] == -1 and arr[i][1] >= num_to_move):
      arr = [x if x[0] != to_move else (-1, x[1]) for x in arr]
      j = 0
      while j < len(arr) - 1:
        if arr[j][0] == -1 and arr[j+1][0] == -1:
          arr = arr[:j] + [(-1, arr[j][1] + arr[j+1][1])] + arr[j+2:]
        else:
          j += 1
      arr = arr[:i] + [(to_move, num_to_move), (-1, arr[i][1] - num_to_move)] + arr[i + 1:]
      break
  to_move -= 1

idx = 0
for x in arr:
  for i in range(x[1]):
    if x[0] > -1:
      out += idx * x[0]
    idx += 1

print(out)
