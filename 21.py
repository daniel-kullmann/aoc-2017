import re

def reverse(list):
    return list[::-1]

def rotate(matrix):
    return tuple(map(lambda p: "".join(p), zip(*matrix[::-1])))

def flipH(matrix):
    return tuple(map(reverse,matrix))

def flipV(matrix):
    return tuple(reverse(matrix))

def flipHV(matrix):
    return flipH(flipV(matrix))

def parse(input):
    result = {}
    for item in input:
        (a,b) = item.strip().split(" => ")
        a1 = tuple(a.split("/"))
        a2 = rotate(a1)
        a3 = rotate(a2)
        a4 = rotate(a3)
        a5 = flipH(a1)
        a6 = flipH(a2)
        a7 = flipH(a3)
        a8 = flipH(a4)
        b = tuple(b.split("/"))
        result[a1] = b
        result[a2] = b
        result[a3] = b
        result[a4] = b
        result[a5] = b
        result[a6] = b
        result[a7] = b
        result[a8] = b
    return result

def break_up(image, square_size):
    pieces = len(image) / square_size
    result = []
    for ySquare in range(0, pieces):
        rows = image[ySquare*square_size:(ySquare+1)*square_size]
        squareRow = []
        for xSquare in range(0, pieces):
            square = [row[xSquare*square_size:(xSquare+1)*square_size] for row in rows]
            squareRow.append(square)
        result.append(map(tuple,squareRow))
    return result

def convert(image, rules):
    #print "convert"
    #print image, rotate(image), rotate(rotate(image)), rotate(rotate(rotate(image)))
    return rules.get(tuple(image), image)

# [["..","..",".."], ["..","..",".."]]
def combine(sub_images):
    result = []
    for row in sub_images:
        for single_row in range(0, len(row[0])):
            result.append("".join([r[single_row] for r in row]))
    return result
    
fh = open("21.txt")
input = [s.strip() for s in fh.readlines()]
fh.close()
rules = parse(input)

#for a in rules.keys(): print a, "->", rules[a]

image = tuple(".#./..#/###".split("/"))
#image = ".#../..#./###./#.#.".split("/")

for iteration in range(0,18):
    square_size = None
    if len(image) % 2 == 0:
        square_size = 2
    elif len(image) % 3 == 0:
        square_size = 3
    else:
        raise Exception("size: " + str(len(image)))
    num_squares = len(image) / square_size
    #print "# Image"
    #print "\n".join(image) + "\n"
    sub_images = break_up(image, square_size)
    #print "# Sub Images"
    #print sub_images
    #for sub in sub_images: 
    #    for s2 in sub: 
    #        print "\n".join(s2) + "\n"
    converted_subs = [[convert(s2, rules) for s2 in sub] for sub in sub_images]
    #print "# Converted Sub Images"
    #print converted_subs
    #for sub in converted_subs: 
    #    for s2 in sub:
    #        print "\n".join(s2) + "\n"
    
    image = combine(converted_subs)
    #print "# Result Image"
    #print "\n".join(image) + "\n"
    if iteration == 4:
        print len(filter(lambda p: p == "#", "".join(image)))

#print "# Image"
#print "\n".join(image) + "\n"
print len(filter(lambda p: p == "#", "".join(image)))

