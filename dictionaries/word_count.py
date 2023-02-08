f = open("tiny_tale.txt", "r")
counts = {}
for line in f:
    words = line[0:-1].split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

print(counts)

for word,count in counts.items():
    print(f"{word:>20} : {count}")
