import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

def step(old, factor):
  return ((old * factor) ^ factor) % 16777216

def next(old):
  n = ((old * 64) ^ old) % 16777216
  n = ((n // 32) ^ n) % 16777216
  return ((n * 2048) ^ n) % 16777216

for line in open(fname):
  line = int(line.strip())
  n = line
  for i in range(2000):
    n = next(n)
  out += n

print(out)
