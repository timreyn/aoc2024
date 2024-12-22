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

scores = collections.defaultdict(int)

for line in open(fname):
  line = int(line.strip())
  n = line
  old = n
  deltas = []
  seen = set()

  for i in range(2000):
    n = next(n)
    deltas += [(n % 10) - (old % 10)]
    old = n
    if len(deltas) < 4:
      continue
    if len(deltas) > 4:
      deltas = deltas[1:]
    if tuple(deltas) in seen:
      continue
    seen.add(tuple(deltas))
    scores[tuple(deltas)] += n % 10

mv = 0
mk = 0
for k,v in scores.items():
  if v > mv:
    mv = v
    mk = k

print(mk)
print(mv)
