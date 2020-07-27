astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('Bob')
except:
    istr = -1
print('Done', istr)

# More practical example of try-except

rawstr = input('Enter your number:')

try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')
