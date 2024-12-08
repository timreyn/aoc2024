import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
grid = []
antennas = collections.defaultdict(list)
antinodes = set()

def is_valid(pt, grid):
  return pt[0] >= 0 and pt[0] < len(grid) and pt[1] >= 0 and pt[1] < len(grid)

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
      antinode = p1
      while is_valid(antinode, grid):
        antinodes.add(antinode)
        antinode = (antinode[0] + p1[0] - p2[0], antinode[1] + p1[1] - p2[1])

print(len(antinodes))
