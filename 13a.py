import re
fh = open("13.txt")
items = fh.readlines()
fh.close()

test_items = """0: 3
1: 2
4: 4
6: 4""".split("\n")

line_regex = re.compile("""([0-9]+): ([0-9]+)?""")
firewall = {}
for item in items:
    if item.strip() == "": continue
    match = line_regex.match(item.strip())
    if match != None:
        layer = int(match.group(1))
        depth = int(match.group(2))
        firewall[layer] = depth
    else:
        raise Exception("ERROR: " + item)

def incState(state, firewall):
    for layer in firewall.keys():
        (value, direction) = state[layer]
        if direction == "down":
            value = value + 1
            if value == firewall[layer] -1:
                direction = "up"
        elif direction == "up":
            value = value - 1
            if value == 0:
                direction = "down"
        else:
            raise Exception("state: " + str((value, direction)))
        state[layer] = (value, direction)

def run(firewall, state):
        
    incState(state, firewall)
    savedState = state.copy()

    severity = 0
    maxLayer = max(firewall.keys())
    for currentLayer in range(0, maxLayer+1):
        # test
        currentState = state.get(currentLayer)
        if currentState != None and currentState[0] == 0:
            severity = 1000
            break
        # next state
        incState(state, firewall)
    return (savedState, severity)

state = {}
for layer in firewall.keys():
    state[layer] = (0, "down")
delay = 0
while True:
    (state, result) = run(firewall, state)
    delay += 1
    #print delay, result
    if result == 0:
        print "result", delay
        break
    if delay % 100000 == 0:
        print delay
