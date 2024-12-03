import collections
import re
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
active = True

for line in open(fname):
  line = line.strip()
  for i in range(len(line)):
    l = line[i:]
    if l.startswith('do()'):
      active = True
    elif l.startswith('don\'t()'):
      active = False
    elif active and l.startswith('mul('):
      match = re.match('^mul\((\d*),(\d*)\)', l)
      if match:
        out += int(match.group(1)) * int(match.group(2))


print(out)
