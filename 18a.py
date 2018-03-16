import re

NUMBER = re.compile(r"^-?\d+$")

def parse(asm):
    program = []
    for line in asm:
        items = line.split()
        program.append(items)
    return program


def get(what, registers):
    if NUMBER.match(what) != None:
        return int(what)
    return registers.get(what, 0)

def step(program, state, otherPipe):
    (pc, waiting, pipe, registers, sendCount, name) = state
    waiting = False
    
    pc_was_set = False
    command = ()
    if pc >= 0 and pc < len(program):
        command = program[pc]
    else:
        state[1] = True # simulate stopped process
        return state
    #print name, pc, " ".join(command), registers, [get(s, registers) for s in command[1:]]
    mnemonic = command[0]
    if mnemonic == "snd":
        value = get(command[1], registers)
        otherPipe.append(value)
        print name, "sent", value
        sendCount += 1
    elif mnemonic == "set":
        registers[command[1]] = get(command[2], registers)
    elif mnemonic == "add":
        registers[command[1]] = get(command[1], registers) + get(command[2], registers)
    elif mnemonic == "mul":
        registers[command[1]] = get(command[1], registers) * get(command[2], registers)
    elif mnemonic == "mod":
        registers[command[1]] = get(command[1], registers) % get(command[2], registers)
    elif mnemonic == "rcv":
        if get(command[1], registers) != 0:
            if len(pipe) > 0:
                o = pipe
                value = pipe[0]
                registers[command[1]] = value
                pipe = pipe[1:]
                print name, "received", value, len(o), len(pipe)
            else:
                pc_was_set = True # i.e. just stay at this pc
                print name, "is waiting"
                waiting = True
    elif mnemonic == "jgz":
        if get(command[1], registers) > 0:
            pc += get(command[2], registers)
            pc_was_set = True
    if not pc_was_set:
        pc += 1
    return [pc, waiting, pipe, registers, sendCount, name]

fh = open("18.txt")
#fh = open("18.test")
asm = [s.strip() for s in fh.readlines()]
fh.close()
program = parse(asm)

state1 = [0, None, [], {"p": 0}, 0, "0"]
state2 = [0, None, [], {"p": 1}, 0, "1"]

while True:
    state1 = step(program, state1, state2[2])
    state2 = step(program, state2, state1[2])
    if state1[1] == True and state2[1] == True:
        # both programs wait on each other -> deadlock!
        break

print state1
print state2
(pc, waiting, pipe, registers, sendCount, name) = state2
print sendCount
