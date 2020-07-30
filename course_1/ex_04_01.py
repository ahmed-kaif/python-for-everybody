# program to compute a worker's gross pay using function

def computepay(hour, rate):
    h = float(hour)
    r = float(rate)
    if h > 40.0:
        extra_hrs = h - 40.0
        extra_rate = r * 1.5
        extra_pay = extra_hrs * extra_rate
        total_pay = (40.0 * r) + extra_pay
    else:
        total_pay = h * r
    return total_pay


hrs = input("Enter Hours:")
rate = input("Enter Rate:")

pay = computepay(hrs, rate)

print('Pay', pay)
