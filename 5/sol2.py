import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

found_blank = False

rules = collections.defaultdict(list)

for line in open(fname):
  line = line.strip()
  if not found_blank:
    if not line:
      found_blank = True
    else:
      spl = line.split('|')
      rules[int(spl[0])] += [int(spl[1])]
  else:
    spl = [int(x) for x in line.split(',')]
    works = True
    for i, x in enumerate(spl):
      for j, y in enumerate(spl):
        if i < j:
          continue
        if y in rules[x]:
          works = False
    if not works:
      bank = [x for x in spl]
      l = []
      while bank:
        for a in bank:
          can_be_used = True
          for b in bank:
            if a in rules[b]:
              can_be_used = False
          if can_be_used:
            l += [a]
            bank = [x for x in bank if x != a]
      out += l[len(l) // 2]

print(out)
