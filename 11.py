fh = open("11.txt")
input = fh.readline().strip().split(",")

def steps(input):

    map = dict()
    for direction in input:
        if direction not in map:
            map[direction] = 0
        map[direction] += 1

    m = dict()

    # Going n and s cancel each other out
    if map["n"] > map["s"]:
        m["n"] = map["n"] - map["s"]
        m["s"] = 0
    else:
        m["s"] = map["s"] - map["n"]
        m["n"] = 0
    
    # Going nw and se cancel each other out
    if map["nw"] > map["se"]:
        m["nw"] = map["nw"] - map["se"]
        m["se"] = 0
    else:
        m["se"] = map["se"] - map["nw"]
        m["nw"] = 0

    # Going ne and sw cancel each other out
    if map["ne"] > map["sw"]:
        m["ne"] = map["ne"] - map["sw"]
        m["sw"] = 0
    else:
        m["sw"] = map["sw"] - map["ne"]
        m["ne"] = 0

    # Going ne and nw is like going n
    if m["ne"] > 0 and m["nw"] > 0:
        minValue = min(m["ne"], m["nw"])
        m["ne"] -= minValue
        m["nw"] -= minValue
        m["n"] += minValue
    
    # Going se and sw is like going s
    if m["se"] > 0 and m["sw"] > 0:
        minValue = min(m["se"], m["sw"])
        m["se"] -= minValue
        m["sw"] -= minValue
        m["s"] += minValue

    # Going ne and s is like going se
    if m["ne"] > 0 and m["s"] > 0:
        minValue = min(m["ne"], m["s"])
        m["ne"] -= minValue
        m["s"] -= minValue
        m["se"] += minValue

    # Going nw and s is like going sw
    if m["nw"] > 0 and m["s"] > 0:
        minValue = min(m["nw"], m["s"])
        m["nw"] -= minValue
        m["s"] -= minValue
        m["sw"] += minValue

    # Going se and n is like going ne
    if m["se"] > 0 and m["n"] > 0:
        minValue = min(m["se"], m["n"])
        m["se"] -= minValue
        m["n"] -= minValue
        m["ne"] += minValue

    # Going sw and n is like going nw
    if m["sw"] > 0 and m["n"] > 0:
        minValue = min(m["sw"], m["n"])
        m["sw"] -= minValue
        m["n"] -= minValue
        m["nw"] += minValue

    return sum(m.values())

print steps(input)
