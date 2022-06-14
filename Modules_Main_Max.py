import Modules_Max

numbers = []
for i in range(1, 6):
    digits = int(input(f"Write {i} Digit: "))
    numbers.append(digits)

# numbers += input("Write some Digit separated by space: ").split()

print(f"Max number is: {Modules_Max.find_max(numbers)}")
