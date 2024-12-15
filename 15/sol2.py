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
    l = []
    for x in line:
      if x == '#':
        l += ['#', '#']
      elif x == 'O':
        l += ['[', ']']
      elif x == '.':
        l += ['.', '.']
      elif x == '@':
        pos = (len(grid), len(l))
        l += ['@', '.']
    grid += [l]
  else:
    moves += [x for x in line]

dirs = {'<': (0, -1), '>': (0,1), 'v': (1,0), '^': (-1, 0)}

def p(a, b):
  return (a[0] + b[0], a[1] + b[1])

def get(grid, p):
  return grid[p[0]][p[1]]

def set(grid, p, v):
  grid[p[0]][p[1]] = v

def recursively_add_move(grid, moves, old, d):
  new = p(old, d)
  if old not in moves:
    moves[old] = '.'
  if get(grid, new) == '.':
    moves[new] = get(grid, old)
    return True
  elif get(grid, new) == '#':
    return False
  elif d[0] == 0:
    moves[new] = get(grid, old)
    return recursively_add_move(grid, moves, new, d)
  elif get(grid, new) == '[':
    moves[new] = get(grid, old)
    return recursively_add_move(grid, moves, new, d) and recursively_add_move(grid, moves, p(new, (0,1)), d)
  elif get(grid, new) == ']':
    moves[new] = get(grid, old)
    return recursively_add_move(grid, moves, new, d) and recursively_add_move(grid, moves, p(new, (0,-1)), d)


for move in moves:
  d = dirs[move]
  moves_to_do = {}
  if recursively_add_move(grid, moves_to_do, pos, d):
    for k,v in moves_to_do.items():
      set(grid, k, v)
    pos = p(pos, d)

for line in grid:
  print(''.join(line))
print()

for i in range(len(grid)):
  for j in range(len(grid[i])):
    if get(grid, (i,j)) == '[':
      gps = 100 * i + j
      out += gps

print(out)
