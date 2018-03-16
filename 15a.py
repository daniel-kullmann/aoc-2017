modulo = 2147483647
aFactor = 16807
bFactor = 48271
aCheck = 4
bCheck = 8

def step(value, factor, check):
    while True:
        value = (value*factor) % modulo
        if (value % check) == 0:
            return value
    
def generate():
    aValue = 512
    bValue = 191
    #aValue = 65
    #bValue = 8921
    count = 0
    for n in range(0, 5*1000*1000):
        aValue = step(aValue, aFactor, aCheck)
        bValue = step(bValue, bFactor, bCheck)
        if (aValue % 65536) == (bValue % 65536):
            count += 1
            print count, n, aValue, bValue
    print count

generate()


        

    