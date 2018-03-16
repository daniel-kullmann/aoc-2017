modulo = 2147483647
aFactor = 16807
bFactor = 48271


def step(value, factor):
    return (value*factor) % modulo
    
def generate():
    aValue = 512
    bValue = 191
    #aValue = 65
    #bValue = 8921
    count = 0
    for n in range(0, 40*1000*1000):
        aValue = step(aValue, aFactor)
        bValue = step(bValue, bFactor)
        if (aValue % 65536) == (bValue % 65536):
            count += 1
            print count, n, aValue, bValue
    print count

generate()


        

    