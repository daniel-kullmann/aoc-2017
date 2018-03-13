def generator(s):
    result = { (0,0): 1 }
    k = 2
    n = 2
    x = 0
    y = 0
    while k <= s:
        side_length = 2*k - 1
        x+=1
        result[(x,y)] = n
        n+=1
        for a in range(0,side_length-2):
            y-=1
            result[(x,y)] = n
            n+=1
        for a in range(0,side_length-1):
            x-=1
            result[(x,y)] = n
            n+=1
        for a in range(0,side_length-1):
            y+=1
            result[(x,y)] = n
            n+=1
        for a in range(0,side_length-1):
            x+=1
            result[(x,y)] = n
            n+=1
        k += 1
    return result


def pp(data):
    maxValue = max(data.values())
    valueSize = len(str(maxValue)) + 1
    minX = min([x for (x,y) in data.keys()])
    minY = min([y for (x,y) in data.keys()])
    for y in range(minY, -minY+1):
        for x in range(minX, -minX+1):
            s = str(data[(x,y)])
            s = s + " "*(valueSize-len(s))
            print s,
        print ""        

data = generator(6)     
print(pp(data))
