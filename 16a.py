import sys

def parse_dance():
    fh = open("16.txt")
    input = fh.readline().split(",")
    fh.close()
    
    dance = []
    for item in input:
        if item[0] == "s":
            dance.append(("spin", int(item[1:]), -1))
        elif item[0] == "x":
            (i1,i2) = [int(s) for s in item[1:].split("/")]
            dance.append(("exchange", i1, i2))
        elif item[0] == "p":
            (p1,p2) = [s for s in item[1:].split("/")]
            dance.append(("partner", p1, p2))
        else:
            raise Exception("parse " + str(item))
    return dance

def initial_state():
    return [s for s in "abcdefghijklmnop"]

dance = parse_dance()

#dance = [("spin", 1, -1), ("exchange", 3, 4), ("partner", "e", "b")]
#state = [s for s in "abcde"]

def calculate_permutation(state, dance):
    original_state = state[:]
    for (type, p1, p2) in dance:
        if type == "spin":
            split = len(state)-p1
            state = state[split:] + state[0:split]
        elif type == "exchange":
            temp = state[p1]
            state[p1] = state[p2]
            state[p2] = temp
        elif type == "partner":
            i1 = state.index(p1)
            i2 = state.index(p2)
            temp = state[i1]
            state[i1] = state[i2]
            state[i2] = temp
        else:
            raise Exception("item " + str(item))
    
    permutation = []
    for p in state:
        permutation.append(original_state.index(p))
    #print state
    #print permutation    
    return permutation

state = initial_state()
permutation = calculate_permutation(state, dance)

n = 0
state = initial_state()
while n < 1000*1000*1000:
    n+=1
    state = [state[p] for p in permutation]
    #print "".join(state)
    #if n > 2: break

print "".join(state)

# kblheigpmjdafnoc is the wrong answer
