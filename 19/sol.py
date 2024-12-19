import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
available = []

def is_possible(pattern, available):
  if not pattern:
    return True
  for av in available:
    if pattern.startswith(av) and is_possible(pattern[len(av):], available):
      return True
  return False

for line in open(fname):
  line = line.strip()
  if not available:
    available = [x.strip() for x in line.split(',')]
    continue
  if not line:
    continue
  if is_possible(line, available):
    out += 1

print(out)
