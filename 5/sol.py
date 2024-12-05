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
    if works:
      out += spl[len(spl) // 2]

print(out)
