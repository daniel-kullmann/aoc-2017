fh = open("19.txt")
maze = [s for s in fh.readlines()]
fh.close()
y = 0
x = maze[0].index("|")
height = len(maze)
width = len(maze[0])
direction = "s"
letters = []
steps = 0

while True:
    spot = maze[y][x]
    print y, x, spot, direction
    if spot not in "+-| ":
        letters.append(spot)
    if direction == "s":
        if spot not in ("+", " "):
            y += 1
        elif spot == "+":
            if x>0 and maze[y][x-1] != " ":
                direction = "w"
                x -= 1
            elif x<width-1 and maze[y][x+1] != " ":
                direction = "e"
                x += 1
            else:
                raise Exception("state " + str((direction,x,y,spot)))
        else:
            break
            raise Exception("state " + str((direction,x,y,spot)))
    elif direction == "n":
        if spot not in ("+", " "):
            y -= 1
        elif spot == "+":
            if x>0 and maze[y][x-1] != " ":
                direction = "w"
                x -= 1
            elif x<width-1 and maze[y][x+1] != " ":
                direction = "e"
                x += 1
            else:
                raise Exception("state " + str((direction,x,y,spot)))
        else:
            raise Exception("state " + str((direction,x,y,spot)))
    elif direction == "e":
        if spot not in ("+", " "):
            x += 1
        elif spot == "+":
            if y>0 and maze[y-1][x] != " ":
                direction = "n"
                y -= 1
            elif y<height-1 and maze[y+1][x] != " ":
                direction = "s"
                y += 1
            else:
                raise Exception("state " + str((direction,x,y,spot)))
        else:
            raise Exception("state " + str((direction,x,y,spot)))
    elif direction == "w":
        if spot not in ("+", " "):
            x -= 1
        elif spot == "+":
            if y>0 and maze[y-1][x] != " ":
                direction = "n"
                y -= 1
            elif y<height-1 and maze[y+1][x] != " ":
                direction = "s"
                y += 1
            else:
                raise Exception("state " + str((direction,x,y,spot)))
        else:
            raise Exception("state " + str((direction,x,y,spot)))
    else:
        raise Exception("state " + str((direction,x,y,spot)))
    steps += 1

print "".join(letters)
print steps