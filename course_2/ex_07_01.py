# reads a file words.txt and prints all in uppercase

fname = input('Enter your filename: ')
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)