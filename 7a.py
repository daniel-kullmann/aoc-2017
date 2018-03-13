import re
fh = open("7.txt")
items = fh.readlines()
testitems = [
  "pbga (66)",
  "xhth (57)",
  "ebii (61)",
  "havc (66)",
  "ktlj (57)",
  "fwft (72) -> ktlj, cntj, xhth",
  "qoyq (66)",
  "padx (45) -> pbga, havc, qoyq",
  "tknk (41) -> ugml, padx, fwft",
  "jptl (61)",
  "ugml (68) -> gyxo, ebii, jptl",
  "gyxo (61)",
  "cntj (57)",
]
fh.close()

line_regex = re.compile("""([a-z]+) \\(([0-9]+)\\)( -> (.*))?""")
input = []
for item in items:
    match = line_regex.match(item.strip())
    if match != None:
        name = match.group(1)
        weight = int(match.group(2))
        above = []
        if match.group(4) != None:
            above = [s.strip() for s in match.group(4).split(",")]
        input.append((name, weight, above))
    else:
        raise "ERROR: " + item



def calculate_weight(thename):
    return [
        weight + sum([
            calculate_weight(above) for above in aboves
        ]) for (name, weight, aboves) in input if name == thename
    ][0]
    

#print input
for (name, weight, aboves) in input:
    substacks = [calculate_weight(above) for above in aboves]
    if len(substacks) > 0:
        if sum(substacks) != len(substacks) * substacks[0]:
            print name, substacks
    
