import re
fh = open("8.txt")
lines = fh.readlines()
test_lines = [
  "b inc 5 if a > 1", 
  "a inc 1 if b < 5", 
  "c dec -10 if a >= 1", 
  "c inc -20 if c == 10"
]
fh.close()

line_regex = re.compile("""([a-z]+) (inc|dec) (-?[0-9]+) if ([a-z]+) ([<>=!]+) (-?[0-9]+)""")
program = []
for line in lines:
    #print line.strip()
    match = line_regex.match(line.strip())
    if match != None:
        target = match.group(1)
        type = match.group(2)
        diff = int(match.group(3))
        compare1 = match.group(4)
        comparison = match.group(5)
        compare2 = int(match.group(6))
        program.append((target, type, diff, compare1, comparison, compare2))
    else:
        raise Exception("asm: " + line.strip())


registers = {}
for (target, type, diff, compare1, comparison, compare2) in program:
    value1 = registers.get(compare1, 0)
    comparison_result = False
    if comparison == "==":
        comparisonResult = value1 == compare2
    elif comparison == ">=":
        comparisonResult = value1 >= compare2
    elif comparison == "<=":
        comparisonResult = value1 <= compare2
    elif comparison == "<":
        comparisonResult = value1 < compare2
    elif comparison == ">":
        comparisonResult = value1 > compare2
    elif comparison == "!=":
        comparisonResult = value1 != compare2
    else:
        raise Exception("comparison: " + str((target, diff, compare1, comparison, compare2)))
    
    if comparisonResult:
        if type == "inc":
            registers[target] = registers.get(target, 0) + diff
        elif type == "dec":
            registers[target] = registers.get(target, 0) - diff
        else:
            raise Exception("type: " + str((target, diff, compare1, comparison, compare2)))
            
print max(registers.values())