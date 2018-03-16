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

def run(firewall):
    state = {}
    for layer in firewall.keys():
        state[layer] = (0, "down")
        
    maxLayer = max(firewall.keys())
    
    penalty = 0
    for currentLayer in range(0, maxLayer+1):
        # test
        #print currentLayer, state.get(currentLayer, -1)
        currentState = state.get(currentLayer)
        if currentState != None and currentState[0] == 0:
            penalty += currentLayer * firewall[currentLayer]
        # next state
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
    return penalty

print run(firewall)