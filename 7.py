import re
fh = open("7.txt")
items = fh.readlines()
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

start = input[0][0]
while True:
    below = [name for (name, weight, above) in input if start in above]
    if len(below) == 0:
        break
    start = below[0]
print start
