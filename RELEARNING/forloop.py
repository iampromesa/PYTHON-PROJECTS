prices = int(input("Input five numbers seperated with commas: "))
total = 0

for price in prices:
    total += price
print("Total: {}".format(total))
