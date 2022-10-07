score = int(input("Enter a number greater than 10: "))
pay = 0

if score > 90:
    pay *= 3
    print("Pay is {}".format(pay))
else:
    pay *= 1
    print("Pay is {}".format(pay))