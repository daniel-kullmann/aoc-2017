import re

#p=<1609,-863,-779>, v=<-15,54,-69>, a=<-10,0,14>
REGEX = re.compile(r"p=<([-,0-9]+)>, v=<([-,0-9]+)>, a=<([-,0-9]+)>")

def parse(input):
    result = []
    p_no = 0
    for item in input:
        match = REGEX.match(item.strip())
        if match != None:
            position = map(int, match.group(1).split(","))
            velocity = map(int, match.group(2).split(","))
            acceleration = map(int, match.group(3).split(","))
            result.append([0, position, velocity, acceleration, p_no])
        else:
            raise Exception("parse " + item)
        p_no += 1
    return result

fh = open("20.txt")
input = [s.strip() for s in fh.readlines()]
fh.close()
particles = parse(input)


particles.sort(key=lambda x: sum(map(abs,x[3])))
for p in particles[0:10]: print p
import sys
sys.exit(1)

cycle=0
while True:
    for p in particles:
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
        #print number, new_distance
        p[0] = new_distance
    cycle+=1
    if cycle>20000: break

print cycle

particles.sort(key=lambda x: x[0])
for p in particles[0:10]: print p
