import collections
import sys
import functools

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
available = []

@functools.cache
def is_possible(pattern):
  global available
  if not pattern:
    return 1
  out = 0
  for av in available:
    if pattern.startswith(av):
      out += is_possible(pattern[len(av):])
  return out

for line in open(fname):
  line = line.strip()
  if not available:
    available = [x.strip() for x in line.split(',')]
    continue
  if not line:
    continue
  out += is_possible(line)

print(out)
