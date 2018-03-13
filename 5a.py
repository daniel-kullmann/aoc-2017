fh = open("5.txt")
program = [int(line) for line in fh.readlines()]
fh.close()

pc = 0
steps = 0
while pc >= 0 and pc < len(program):
    jump = program[pc]
    if jump >= 3:
        program[pc] -= 1
    else:
        program[pc] += 1
    pc += jump
    steps += 1
    
print pc
print steps