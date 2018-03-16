def parse(asm):
    program = []
    for line in asm:
        items = line.split()
        program.append(items)
    return program


def get(what, registers):
    if what not in "abcdefghijklmnopqrstuvwxyz":
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
        #print name, "sent", value
        sendCount += 1
    elif mnemonic == "set":
        registers[command[1]] = get(command[2], registers)
    elif mnemonic == "add":
        registers[command[1]] += get(command[2], registers)
    elif mnemonic == "mul":
        registers[command[1]] *= get(command[2], registers)
    elif mnemonic == "mod":
        registers[command[1]] %= get(command[2], registers)
    elif mnemonic == "rcv":
        if len(pipe) > 0:
            value = pipe.pop(0)
            registers[command[1]] = value
            #print name, "received", value, len(pipe)
        else:
            pc_was_set = True # i.e. just stay at this pc
            #print name, "is waiting"
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

state0 = [0, None, [], {"p": 0}, 0, "0"]
state1 = [0, None, [], {"p": 1}, 0, "1"]

while True:
    state0 = step(program, state0, state1[2])
    state1 = step(program, state1, state0[2])
    if state0[1] == True and state1[1] == True:
        # both programs wait on each other -> deadlock!
        break

print state0
print state1
(pc, waiting, pipe, registers, sendCount, name) = state1
print sendCount
