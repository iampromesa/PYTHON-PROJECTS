numbers = [5,5,2,2,5,4,3,7,7]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)