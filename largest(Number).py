numbers = [10, 25, 7, 55, 18]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number =", largest)