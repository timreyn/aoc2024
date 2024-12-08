import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
grid = []
antennas = collections.defaultdict(list)
antinodes = set()

for line in open(fname):
  i = len(grid)
  line = line.strip()
  grid += [line]
  for j, val in enumerate(line):
    if val != '.':
      antennas[val] += [(i, j)]

for k in antennas.keys():
  for p1 in antennas[k]:
    for p2 in antennas[k]:
      if p1 == p2:
        continue
      antinode = (p1[0] * 2 - p2[0], p1[1] * 2 - p2[1])
      if antinode[0] < 0 or antinode[0] >= len(grid) or antinode[1] < 0 or antinode[1] >= len(grid):
        continue
      antinodes.add(antinode)

print(len(antinodes))
