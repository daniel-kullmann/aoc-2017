
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
    value = bin(int(hex, 16))[2:])
    while len(value)

input = "amgozmfv"
input = "flqrgnkx"
for row in range(0, 128):
    hash = knot_hash(input+"-"+str(row))
    print hash
