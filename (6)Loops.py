
# -->Loop<-- #
# i = 1
# while i <= 5:
#     print("*" * i)
#     i = i + 1
# print("Done!!")

# guess_number = 5
# i = 1
# count = 2
# while (i <= 3):
#     user_guess = int(input("Guess a number: "))
#     i = i+1
#     if user_guess == guess_number:
#         print(f"{user_guess} is Right. You Win!!")
#         break
#     else:
#         print(f"{user_guess} is Wrong. Try Again!! {count} chance left")
#     count = count-1
# else:
#     print("You Failed to guess")

# started = False
# while True:
#     command = input("Write Something: ").upper()
#     if command == "START":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car Started...")
#     elif command == "STOP":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car Stopped.")
#     elif command == "HELP":
#         print("""
# Type (start) --> To start the car
# Type (stop) --> To stop the car
# Type (quit) --> To exit the program
# """)
#     elif command == "QUIT":
#         print("The Program is exits")
#         break
#     else:
#         print("Sorry i don't understand you...")

# for name in "Nasif":
#     print(name)
# for names in ["Nasif", "Azam", "Zisha"]:
#     print(names)
# names = ["Nasif", "Azam", "Zisha"]
# names[2] = "Jarin"
# print(names)
# print(names[0:2])
# for num in [1, 2, 3, 4, 5]:
#     print(num)
# for numbers in range(2, 20, 2):  # range(start,end,difference)
#     print(numbers)

# prices = [10, 20, 30]
# total = 0
# for product in prices:
#     total = total + product
# print(f"Total: {total}")

# Nested Loops
for x in range(1, 4):
    for y in range(1, 3):
        print(f"({x},{y})")

# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     print("X"*x)

numbers = [5, 2, 2, 3, 2, 2]
for x in numbers:
    output = ""
    for count in range(x):
        output = output + "x"
    print(output)

# Find Largest Number
numbers = [2, 85, 41, 78, 5, 14, 5, 3, 44]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(f"Max: {max}")
