import re

fname = input('Enter File name: ')
fh = open(fname)
sum = 0
for line in fh:
    nums = re.findall("[0-9]+", line)  # finds numbers in the line
    for num in nums:
        sum = sum + int(num)  # for each line the numbers are added in sum

print('Sum =', sum)
