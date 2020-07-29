# dictonary type in python

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)

counts = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        line = line.rstrip()
        pieces = line.split()
        words = pieces[1]
        counts[words] = counts.get(words, 0) + 1


bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print(bigWord, bigCount)
