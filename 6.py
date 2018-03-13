fh = open("6.txt")
banks = [int(item) for item in fh.readline().split()]
fh.close()
#banks = [0, 2, 7, 0]

numBanks = len(banks)
configs = []
cycles = 0
while banks not in configs:
    configs.append(banks[:])
    maxValue = max(banks)
    index = [i for i in range(0, numBanks) if banks[i] == maxValue][0]
    #print banks, index
    banks[index] = 0
    for extra in range(1, maxValue+1):
        banks[(index+extra)%numBanks] += 1
    cycles += 1

print(cycles-configs.index(banks))
