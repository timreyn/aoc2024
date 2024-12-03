import collections
import re
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

for line in open(fname):
  line = line.strip()
  for match in re.findall(r'mul\((\d*),(\d*)\)', line):
    out += int(match[0]) * int(match[1])


print(out)
