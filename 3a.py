def val(data, x, y):
    result = data.get((x,y))
    if result == None: return 0
    return result
def get(data, x, y):
  value = (
      val(data,x-1,y-1) + val(data,x,y-1) + val(data,x+1,y-1) +
      val(data,x-1,y)                     + val(data,x+1,y) +
      val(data,x-1,y+1) + val(data,x,y+1) + val(data,x+1,y+1)
    )
  if value > 312051:
      print "GREATER", value
      import sys
      sys.exit(1)
  return value

def generator(s):
    result = { (0,0): 1 }
    k = 2
    n = 2
    x = 0
    y = 0
    while k <= s:
        side_length = 2*k - 1
        x+=1
        result[(x,y)] = get(result, x, y)
        n+=1
        for a in range(0,side_length-2):
            y-=1
            result[(x,y)] = get(result, x, y)
        for a in range(0,side_length-1):
            x-=1
            result[(x,y)] = get(result, x, y)
        for a in range(0,side_length-1):
            y+=1
            result[(x,y)] = get(result, x, y)
        for a in range(0,side_length-1):
            x+=1
            result[(x,y)] = get(result, x, y)
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

data = generator(100)     
#pp(data)
