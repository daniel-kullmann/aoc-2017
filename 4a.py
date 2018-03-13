fh = open("4.txt")
lines = fh.readlines()
fh.close()

def letterset(word):
    result = dict()
    for c in word:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return ".".join([key + ":" + str(result[key]) for key in sorted(result.keys())])
    
    
count = 0
for pw in lines:
    if pw.strip() == "": continue
    words = pw.strip().split()
    wordset = {letterset(word): 1 for word in words}
    #print words, wordset
    if len(words) == len(wordset):
        count += 1

print(letterset("abc def cba"))
print len(lines)
print count
