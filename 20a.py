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
            result.append([position, velocity, acceleration, p_no, True])
        else:
            raise Exception("parse " + item)
        p_no += 1
    return result

fh = open("20.txt")
input = [s.strip() for s in fh.readlines()]
fh.close()
particles = parse(input)


cycle=0
while True:
    for i1, p1 in enumerate(particles):
        for i2, p2 in enumerate(particles[i1+1:]):
            if p1[0] == p2[0]:
                p1[4] = False
                p2[4] = False
    a = len(particles)
    particles = filter(lambda p: p[4], particles)   
    b = len(particles)
    if a > b:
        print "collisions:", a, "->", b  
    for p in particles:
        position = p[0]
        velocity = p[1]
        acceleration = p[2]
        number = p[3]
        
        for i in range(0,3):
            velocity[i] += acceleration[i]
        p[1] = velocity
        
        for i in range(0,3):
            position[i] += velocity[i]
        p[0] = position
        
    cycle+=1
    if cycle>20000: break

print cycle

particles.sort(key=lambda x: x[0])
for p in particles[0:10]: print p
