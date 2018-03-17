def parse(asm):
    program = []
    for line in asm:
        items = line.split()
        program.append(items)
    return program


def get(what):
    global registers
    if what not in "abcdefgh":
        return int(what)
    return registers.get(what, 0)

def run(program):
    pc = 0
    n = 0
    while pc >= 0 and pc < len(program):
        pc_was_set = False
        command = program[pc]
        #print pc, " ".join(command), registers, [get(s) for s in command[1:]]
        mnemonic = command[0]
        if mnemonic == "set":
            registers[command[1]] = get(command[2])
        elif mnemonic == "sub":
            registers[command[1]] = get(command[1]) - get(command[2])
        elif mnemonic == "mul":
            registers[command[1]] = get(command[1]) * get(command[2])
            n += 1
        elif mnemonic == "jnz":
            if get(command[1]) != 0:
                pc += get(command[2])
                pc_was_set = True
        else:
            raise Exception("instruction " + str(command))
        if not pc_was_set:
            pc += 1
    return n
        
fh = open("23.txt")
#fh = open("23.test")
asm = [s.strip() for s in fh.readlines()]
fh.close()
program = parse(asm)
registers = {"a": 1}
result = run(program)
print result
