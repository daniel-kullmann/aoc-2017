
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

def hex2(number):
    result = hex(number)[2:]
    while len(result) < 2:
        result = "0" + result
    return result

def encode(input):
    return "".join([hex2(i) for i in input])
    
def process(ring, input):
    result = rounds(ring, input)
    return encode(dense_hash(result))
    
ring = range(0,256)
input = [ord(s) for s in ""] + [17, 31, 73, 47, 23]
print process(ring, input)

ring = range(0,256)
input = [ord(s) for s in "AoC 2017"] + [17, 31, 73, 47, 23]
print process(ring, input)

ring = range(0,256)
input = [ord(s) for s in "1,2,3"] + [17, 31, 73, 47, 23]
print process(ring, input)

ring = range(0,256)
input = [ord(s) for s in "1,2,4"] + [17, 31, 73, 47, 23]
print process(ring, input)

ring = range(0,256)
fh = open("10.txt")
input = [ord(s) for s in fh.readline().strip()] + [17, 31, 73, 47, 23]
fh.close()
print process(ring, input)

