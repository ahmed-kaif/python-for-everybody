hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h > 40.0:
    extra_hrs = h - 40.0
    extra_rate = r * 1.5
    extra_pay = extra_hrs * extra_rate
    total_pay = (40.0 * r) + extra_pay
else:
    total_pay = h * r

print(total_pay)
