import sys

def twist(ring, start, length):
    begin = start
    end = (start+length-1)%len(ring)
    steps = length/2
    for s in range(0, steps):
        temp = ring[begin]
        ring[begin] = ring[end]
        ring[end] = temp
        begin = (begin+1) % len(ring)
        end = (end-1) % len(ring)
    return ring

def rounds(input, lengths):
    skip = 0
    position = 0
    for round in range(0, 64):
        for length in lengths:
            if length != 1:
                input = twist(input, position, length)
            #print position, length, input
            position = (position + length + skip) % len(input)
            skip += 1
    return input

def dense_hash(input):
    result = []
    for block_no in range(0,16):
        block = input[16*block_no:16*(block_no+1)]
        single_result = 0
        for entry in block:
            single_result = single_result ^ entry
        result.append(single_result)
    return result

def number2hex(number):
    result = hex(number)[2:]
    while len(result) < 2:
        result = "0" + result
    return result

def encode(input):
    return "".join([number2hex(i) for i in input])
    
def knot_hash(ring, input):
    result = rounds(ring, input)
    return encode(dense_hash(result))
    
def hex2bin(hex):
    value = bin(int(hex, 16))[2:]
    while len(value) < 128:
        value = "0" + value
    return value

input = "amgozmfv"
#input = "flqrgnkx"
grid = []
for row in range(0, 128):
    data = input+"-"+str(row)
    data = [ord(s) for s in data] + [17, 31, 73, 47, 23]
    ring = range(0,256)
    hash = knot_hash(ring, data)
    binary = [s for s in hex2bin(hash).replace("0", ".").replace("1", "#")]
    grid.append(binary)

#for row in grid[0:8]:
#    for cell in row[0:8]:
#        sys.stdout.write(cell)
#    sys.stdout.write("\n")
#sys.stdout.flush()
#for row in grid: print row

def neighbors(y,x):
    result = []
    if y > 0: result.append((y-1, x))
    if y < 127: result.append((y+1, x))
    if x > 0: result.append((y, x-1))
    if x < 127: result.append((y, x+1))
    return result

def flood_fill(grid, sy, sx, group):
    candidates = neighbors(sy,sx)
    grid[sy][sx] = group
    while len(candidates) > 0:
        (y,x) = candidates.pop()
        if grid[y][x] == "#":
            grid[y][x] = group
            candidates += neighbors(y,x)

last_group = 0
for y in range(0, 128):
    for x in range(0, 128):
        if grid[y][x] == "#":
            last_group += 1
            flood_fill(grid, y, x, last_group)

#for row in grid: print row

for row in grid[0:8]:
    for cell in row[0:8]:
        if cell == ".":
            sys.stdout.write(".")
        elif cell == "#":
            raise Exception("# " + str(cell) + " " + str(row))
        else:
            sys.stdout.write(str(cell%10))
    sys.stdout.write("\n")
    sys.stdout.flush()

print last_group
