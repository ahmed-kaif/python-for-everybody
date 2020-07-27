# Assignment 3.3 week 5
score = input("Enter Score: ")
test = float(score)
if test > 1.0:
    print('Sorry.Range is between 0.0 and 1.0')
elif test >= 0.9:
    print('A')
elif test >= 0.8:
    print('B')
elif test >= 0.7:
    print('C')
elif test >= 0.6:
    print('D')
elif test < 0.6:
    if test < 0.0:
        print('Sorry.Range is between 0.0 and 1.0')
    print('F')
