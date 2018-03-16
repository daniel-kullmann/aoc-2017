import re
fh = open("13.txt")
items = fh.readlines()
fh.close()

items = """0: 3
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
            if value == firewall[layer] - 1:
                direction = "up"
        elif direction == "up":
            value = value - 1
            if value == 0:
                direction = "down"
        else:
            raise Exception("state: " + str((value, direction)))
        state[layer] = (value, direction)

def run(firewall, delay):
    
    print firewall
    for d in range(0, delay):
        incState(state, firewall)
        print d, state

    severity = 0
    maxLayer = max(firewall.keys())
    for currentLayer in range(0, maxLayer+1):
        # test
        #print currentLayer, state.get(currentLayer, -1)
        currentState = state.get(currentLayer)
        if currentState != None and currentState[0] == 0:
            severity += currentLayer * firewall[currentLayer]
        # next state
        incState(state, firewall)
    return severity

multiple = 1
for v in firewall.values():
    leastCommonMultiple = lcm(leastCommonMultiple, 2*v)
print leastCommonMultiple

state = {}
for layer in firewall.keys():
    state[layer] = (0, "down")
delay = 0
while True:
    print "##############"
    result = run(firewall, delay)
    print ">>>>", delay, result
    if result == 0:
        print delay
        break
    delay += 1
    if delay >= leastCommonMultiple:
        break
