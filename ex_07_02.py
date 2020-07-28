# reads a file mbox-short.txt and calculates avarage of some specific values
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
val = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.rstrip()
        spcpos = line.find(' ')
        line = line[ spcpos+1 : len(line) ]
        val = val + float(line)
        count = count + 1
    if not line.startswith("X-DSPAM-Confidence:") : continue

avg = val / count
print('Average spam confidence:', avg)