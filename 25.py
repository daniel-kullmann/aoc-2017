import sys

def pp(tape, cursor):
    min_index = min(tape.keys())
    max_index = max(tape.keys())
    for index in xrange(min_index, max_index+1):
        if index == cursor:
            sys.stdout.write("[")
        sys.stdout.write(str(tape[index]))
        if index == cursor:
            sys.stdout.write("]")
        sys.stdout.write(" ")
    sys.stdout.write("\n")
    sys.stdout.flush()
        

fh = open("25.txt")
#fh = open("25.test")
lines = [s.strip() for s in fh.readlines()]
fh.close()

step_line = [line for line in lines if line.startswith("Perform")][0]
num_steps = int(step_line.split(" ")[5])

start_line = [line for line in lines if line.startswith("Begin in state")][0]
start_state = start_line.split(" ")[3].split(".")[0]

#print num_steps, start_state

cursor = 0
tape = {}
state = start_state

for step in xrange(0, num_steps):
    value = tape.get(cursor, 0)
    state_index = lines.index("In state " + state + ":")
    if state_index < 0:
        raise Exception("no such state: " + state)
    value_index = state_index+1 + 4*value
    write_line = lines[value_index+1]
    move_line = lines[value_index+2]
    continue_line = lines[value_index+3]

    new_value = None
    if "the value 1" in write_line:
        new_value = 1
        tape[cursor] = 1
    elif "the value 0" in write_line:
        new_value = 0
        tape[cursor] = 0
    else:
        raise Exception("write line: " + write_line)

    if "to the right" in move_line:
        cursor += 1
    elif "to the left" in move_line:
        cursor -= 1
    else:
        raise Exception("move line: " + move_line)

    if "with state" in continue_line:
        state = continue_line[continue_line.index("state")+6: ].split(".")[0]
    else:
        raise Exception("continue line: " + continue_line)
    
    #print new_value, cursor, state

#print ""
#pp(tape, cursor)
print sum(tape.values()) 