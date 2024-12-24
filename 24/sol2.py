import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
starters = {}
rules = {}

ands = [''] * 100
xors = [''] * 100

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
last_carry = ''

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

swaps = [('z23', 'qqp'),
         ('z36', 'fbq'),
         ('z16', 'pbv'),
         ('qnw', 'qff'),
         #('fjh', 'stw'),
         #('thp', 'qff'),
         ]

l = [x for s in swaps for x in s]
print(','.join(sorted(l)))

for s1,s2 in swaps:
  rr = rules[s1]
  rules[s1] = rules[s2]
  rules[s2] = rr

for r in rules:
  if rules[r][0][1:].isnumeric():
    if rules[r][1] == 'AND':
      ands[int(rules[r][0][1:])] = r
    elif rules[r][1] == 'XOR':
      xors[int(rules[r][0][1:])] = r
  if 'x00' in rules[r] and 'AND' in rules[r] and 'y00' in rules[r]:
    last_carry = [r]

for i in range(max_z + 1):
  if i == 0:
    continue
  a = ands[i - 1]
  b = xors[i]
  z = rules['z' + '%02d' % i]
  #if b not in z:
  #  print('B', i, b, z)
  possible_c = [k for k in rules if rules[k][1] == 'OR' and (a in rules[k] or b in rules[k])]
  possible_d = [k for k in rules if rules[k][1] == 'AND' and (b in rules[k] or len(set(last_carry) & set(rules[k])))]
  last_carry = possible_d
  print(i, a, b, [(c, rules[c]) for c in possible_c], possible_d, rules['z' + '%02d' % i])


print(out)
