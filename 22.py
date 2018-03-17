import sys
def parse(lines):
    grid = {}
    y = -(len(lines) / 2)
    for line in lines:
        x = -(len(lines[0]) / 2)
        for cell in line:
            grid[(y,x)] = cell == "#"
            x +=1
        y += 1
    return grid

def pp(grid):
    min_x = min([x for (y,x) in grid.keys()])
    max_x = max([x for (y,x) in grid.keys()])
    min_y = min([y for (y,x) in grid.keys()])
    max_y = max([y for (y,x) in grid.keys()])
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            sys.stdout.write("#" if grid.get((y,x), False) else ".")
        sys.stdout.write("\n")
    sys.stdout.flush()

directions = "nesw"

def left(direction):
    return directions[(directions.index(direction)-1) % len(directions)]
    
def right(direction):
    return directions[(directions.index(direction)+1) % len(directions)]

def forward(y,x,direction):
    if direction == "n":
        return (y-1, x)
    elif direction == "e":
        return (y, x+1)
    elif direction == "s":
        return (y+1, x)
    elif direction == "w":
        return (y, x-1)
    else:
        raise Exception("forward " + direction)
        
fh = open("22.txt")
#fh = open("22.test")
input = [s.strip() for s in fh.readlines()]
fh.close()

# Grid, key is tuple (y,x), value means True == infected
grid = parse(input)
#pp(grid)
#print grid[(0,0)]

y = 0
x = 0
direction = "n"

num_infections = 0
for step in xrange(0, 10000):
    infected = grid.get((y,x), False)
    if infected:
        direction = right(direction)
    else:
        direction = left(direction)
    grid[(y,x)] = not infected
    if not infected: # i.e. it was just infected
        num_infections += 1
    (y,x) = forward(y, x, direction)

#pp(grid)

print num_infections