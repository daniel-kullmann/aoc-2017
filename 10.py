fh = open("10.txt")
input = [int(s) for s in fh.readline().strip().split(",")]

ring = range(0,256)

def twist(input, start, length):
    begin = start
    end = (start+length-1)%len(input)
    steps = length/2
    for s in range(0, steps):
        temp = input[begin]
        input[begin] = input[end]
        input[end] = temp
        begin = (begin+1) % len(input)
        end = (end-1) % len(input)
    return input

def process(input, lengths):
    skip = 0
    position = 0
    for length in lengths:
        if length != 1:
            input = twist(input, position, length)
        print position, length, input
        position = (position + length + skip) % len(input)
        skip += 1
    return input

#process([0,1,2,3,4], [3,4,1,5])

print input
r = process(ring, input)
print r[0] * r[1]