largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        val = int(num)
        if largest is None:
            largest = val
        elif val > largest:
            largest = val
        if smallest is None:
            smallest = val
        elif val < smallest:
            smallest = val
    except:
        print("Invalid Input")
        continue


print("Maximum is", largest)
print("Minimum is", smallest)
