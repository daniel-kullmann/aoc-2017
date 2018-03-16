skip = 354
#skip = 3

buffer = [0]
position = 0

for n in range(1, 2018):
    position += skip
    position %= len(buffer)
    print position, buffer
    buffer = buffer[:position+1] + [n] + buffer[position+1:]
    print ">", buffer
    position += 1
    if n > 9: break

print buffer[buffer.index(2017)+1]