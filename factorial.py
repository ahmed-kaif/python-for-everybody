# using recursive function to calculate factoorial

def factorial(num):
    result = None
    if num == 0:
        result = 1
        return result
    result = num * factorial(num - 1)
    return result


print('100! =', factorial(100))
i = 1
while i < 4:
    print(str(i)+'! =', factorial(i))
    i = i + 1
