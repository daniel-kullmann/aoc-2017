skip = 354
#skip = 3

position = 0
numberAfterZero = None

for n in range(1, 50000000+1):
    position += skip
    position %= n # n is size of old buffer
    # number is inserted after position
    if position == 0:
        numberAfterZero = n
    position += 1
    #if n > 10: break

print numberAfterZero