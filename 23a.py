h = 0
for x in range(107900,124900 + 1,17):
    for i in range(2,x):
        if x % i == 0:
            h += 1
            break
print(h)
