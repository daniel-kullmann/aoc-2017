skip = 354

buffer = [0]
position = 0

for n in range(1, 2018):
    position += skip
    position %= len(buffer)
    buffer = buffer[:position+1] + [n] + buffer[position+1:]
    #print buffer
    position += 1

print buffer[buffer.index(2017)+1]