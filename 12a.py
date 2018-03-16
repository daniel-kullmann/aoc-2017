import re
fh = open("12.txt")
items = fh.readlines()
fh.close()

test_items = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".split("\n")
    
line_regex = re.compile("""([0-9]+) <-> (.*)?""")
input = {}
for item in items:
    if item.strip() == "": continue
    match = line_regex.match(item.strip())
    if match != None:
        start = int(match.group(1))
        targets = [int(s.strip()) for s in match.group(2).split(",")]
        input[start] = targets
    else:
        raise Exception("ERROR: " + item)

def create_group(program, pipes, seen):
    work_list = [program]
    while len(work_list) > 0:
        work_item = work_list.pop()
        seen[work_item] = 1
        work_list = work_list + [l for l in pipes[work_item] if not l in seen]
    

seen = {}
num_groups = 0
for program in input.keys():
    if program not in seen:
        create_group(program, input, seen)
        num_groups += 1
print num_groups
