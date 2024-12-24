import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
starters = {}
rules = {}

def compute(val):
  if val in starters:
    return starters[val]
  else:
    r = rules[val]
    v1 = compute(r[0])
    v2 = compute(r[2])
    if r[1] == 'AND':
      return 1 if v1 == 1 and v2 == 1 else 0
    elif r[1] == 'OR':
      return 1 if v1 == 1 or v2 == 1 else 0
    elif r[1] == 'XOR':
      return 1 if v1 != v2 else 0

max_z = 0

for line in open(fname):
  line = line.strip()
  if ':' in line:
    l = line.split(':')
    starters[l[0]] = int(l[1])
  elif '->' in line:
    l = line.split(' ')
    rules[l[4]] = [l[0], l[1], l[2]]
    if l[4].startswith('z'):
      max_z = max(max_z, int(l[4][1:]))

for i in range(max_z + 1):
  k = 'z' + '%02d' % i
  out = 2 ** i * compute(k) + out
  print(k, compute(k))

print(out)
