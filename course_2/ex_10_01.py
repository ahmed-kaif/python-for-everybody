name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    else:
        line = line.rstrip()
        line = line.split()
        pieces = line[5]
        hrs = pieces.split(':')[0]
        counts[hrs] = counts.get(hrs, 0) + 1

for (k, v) in sorted(counts.items()):
    print(k, v)
