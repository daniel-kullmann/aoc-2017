import re

NUMBER = re.compile(r"^-?\d+$")

def parse(asm):
    program = []
    for line in asm:
        items = line.split()
        program.append(items)
    return program


def get(what):
    global registers
    if NUMBER.match(what) != None:
        return int(what)
    return registers.get(what, 0)

def run(program):
    last_played_sound = None
    pc = 0
    n = 0
    while pc >= 0 and pc < len(program):
        pc_was_set = False
        command = program[pc]
        #print pc, " ".join(command), registers, [get(s) for s in command[1:]]
        mnemonic = command[0]
        if mnemonic == "snd":
            last_played_sound = get(command[1])
        elif mnemonic == "set":
            registers[command[1]] = get(command[2])
        elif mnemonic == "add":
            registers[command[1]] = get(command[1]) + get(command[2])
        elif mnemonic == "mul":
            registers[command[1]] = get(command[1]) * get(command[2])
        elif mnemonic == "mod":
            registers[command[1]] = get(command[1]) % get(command[2])
        elif mnemonic == "rcv":
            if get(command[1]) != 0:
                return last_played_sound
        elif mnemonic == "jgz":
            if get(command[1]) > 0:
                pc += get(command[2])
                pc_was_set = True
        if not pc_was_set:
            pc += 1
        n += 1
        #if n > 10: return
        
fh = open("18.txt")
#fh = open("18.test")
asm = [s.strip() for s in fh.readlines()]
fh.close()
program = parse(asm)
registers = {}
result = run(program)
print result
