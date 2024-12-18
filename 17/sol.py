import collections
import sys
import re

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = []
registers = {}
program = []

for line in open(fname):
  line = line.strip()
  match = re.match('Register (\\w): (\\d+)', line)
  if match:
    registers[match.group(1)] = int(match.group(2))
  elif 'Program' in line:
    program = [int(x) for x in line.split(':')[1].strip().split(',')]


print(registers)
print(program)
print(oct(registers['A']))
print(bin(registers['A']))

ptr = 0

while ptr < len(program):
  instr = program[ptr]
  ptr += 1
  literal = program[ptr]
  combo = literal
  ptr += 1
  if literal == 4:
    combo = registers['A']
  elif literal == 5:
    combo = registers['B']
  elif literal == 6:
    combo = registers['C']
  if instr == 0:
    cmd = 'adv'
    registers['A'] = registers['A'] >> combo
  elif instr == 1:
    cmd = 'bxl'
    registers['B'] = registers['B'] ^ literal
  elif instr == 2:
    cmd = 'bst'
    registers['B'] = combo % 8
  elif instr == 3:
    cmd = 'jnz'
    if registers['A'] != 0:
      ptr = literal
  elif instr == 4:
    cmd = 'bxc'
    registers['B'] = registers['B'] ^ registers['C']
  elif instr == 5:
    cmd = 'out'
    out += [str(combo % 8)]
    print('output ' + str(combo % 8))
  elif instr == 6:
    cmd = 'bdv'
    registers['B'] = registers['A'] >> combo
  elif instr == 7:
    cmd = 'cdv'
    registers['C'] = registers['A'] >> combo
  print(cmd, combo, literal, registers)

print(','.join(out))
