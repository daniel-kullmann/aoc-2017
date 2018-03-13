fh = open("4.txt")
lines = fh.readlines()
fh.close()

count = 0
for pw in lines:
    if pw.strip() == "": continue
    words = pw.strip().split()
    wordset = {word: 1 for word in words}
    if len(words) == len(wordset):
        count += 1
    
print len(lines)
print count
