fh = open("24.txt")
#fh = open("24.test")
components = [tuple(map(int, s.strip().split("/"))) for s in fh.readlines()]
fh.close()

set = {p for p in components}
if len(set) != len(components):
    raise Exception("no duplicates allowed")

def find(end, nonos=[]):
    return [c for c in components if c not in nonos and (c[0] == end or c[1] == end)]

def other_end(end, component):
    if component[0] == end:
        return component[1]
    elif component[1] == end:
        return component[0]
    else:
        raise Exception("other_end: " + end + " " + str(component))

def strength(bridge):
    return sum(map(sum, bridge))
    
work_list = [([c], other_end(0, c)) for c in find(0)]
finished = []
while len(work_list) > 0:
    (bridge, end) = work_list.pop() 
    #print (bridge, end)
    candidates = find(end, bridge)
    work_list += [(bridge + [candidate], other_end(end, candidate)) for candidate in candidates]
    if len(candidates) == 0:
        finished.append(bridge)


max_length = max(map(len, finished))
#print max_length
#print [f for f in finished if len(f) == max_length]
print max(map(strength, [f for f in finished if len(f) == max_length]))

