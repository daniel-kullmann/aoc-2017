import re

#p=<1609,-863,-779>, v=<-15,54,-69>, a=<-10,0,14>
REGEX = re.compile(r"p=<([-,0-9]+)>, v=<(([-,0-9]+))>, a=<(([-,0-9]+))>")

def parse(input):
    result = []
    p_no = 0
    for item in input:
        match = REGEX.match(item.strip())
        if match != None:
            position = map(int, match.group(1).split(","))
            velocity = map(int, match.group(1).split(","))
            acceleration = map(int, match.group(1).split(","))
            result.append([sum(map(abs,position)), position, velocity, acceleration, p_no])
        else:
            raise Exception("parse " + item)
        p_no += 1
    return result

fh = open("20.txt")
input = [s.strip() for s in fh.readlines()]
fh.close()
particles = parse(input)

#for p in particles: print p

cycle=0
while True:
    got_better = 0
    for p in particles:
        current_distance = p[0]
        position = p[1]
        velocity = p[2]
        acceleration = p[3]
        number = p[4]
        
        for i in range(0,3):
            velocity[i] += acceleration[i]
        p[2] = velocity
        
        for i in range(0,3):
            position[i] += velocity[i]
        p[1] = position
        
        new_distance = sum(map(abs, position))
        print number, current_distance, new_distance
        if new_distance<current_distance:
            got_better += 1
            p[0] = new_distance
    cycle+=1
    print got_better
    if got_better == 0:
        break

print cycle