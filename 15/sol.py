import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
grid = []
switched = False
moves = []
pos = (-1, -1)

for line in open(fname):
  line = line.strip()
  if not line:
    switched = True
  elif not switched:
    l = [x for x in line]
    if '@' in line:
      pos = (len(grid), line.index('@'))
    grid += [l]
  else:
    moves += [x for x in line]

dirs = {'<': (0, -1), '>': (0,1), 'v': (1,0), '^': (-1, 0)}

def p(a, b):
  return (a[0] + b[0], a[1] + b[1])

def get(grid, p):
  return grid[p[0]][p[1]]

for move in moves:
  d = dirs[move]
  immediate_target = p(pos, d)
  target = immediate_target
  while get(grid, target) == 'O':
    target = p(target, d)
  if get(grid, target) == '#':
    continue
  grid[target[0]][target[1]] = 'O'
  grid[immediate_target[0]][immediate_target[1]] = '@'
  grid[pos[0]][pos[1]] = '.'
  pos = immediate_target

for i in range(len(grid)):
  for j in range(len(grid[i])):
    if get(grid, (i,j)) == 'O':
      out += 100 * i + j

print(out)
