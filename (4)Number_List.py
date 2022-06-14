# -->2D lists<-- #
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)

# matrix_string = [
#     ['Nasif', 'Azam', 'Eng'],
#     ['Jarin', 'Zisha', 'Student'],
#     ['Nasif', 'Loves', 'Zisha_Moni']
# ]
# print(matrix_string[0][1])
# for row in matrix_string:
#     for item in row:
#         print(item)

# -->Number List<-- #
# list = [69, 'Nasif', 9.5]
# print(list)
# numbers = [9, 3, 8, 96, 78, 32, 8]
# numbers.append(10)  # Add Item in last
# numbers.insert(0, 30)  # Insert item anywhere
# numbers.remove(8)  # Remove Item
# numbers.clear()  # Clear all item
# numbers.pop(2)  # Removing from last
# print(numbers.index(96))  # Index of an item
# numbers_2 = numbers.copy()  # Copy all item
# print(numbers.count(8)) # Count a number
# numbers.sort()  # Sorting in assending order
# numbers.reverse()  # Sorting in desending order
# print(numbers)

# number = [5, 6, 7, 8, 1, 5, 6, 8, 8]
# uniques = []
# for duplicate in number:
#     if duplicate not in uniques:
#         uniques.append(duplicate)
# print(f"After removing duplicates:\n{uniques}")

# -->Tuples<-- #
# numbers = (1, 2, 3, 4)  # Tuples number never modified
# # numbers[2] = 5
# print(numbers[2])

# -->User Given Fruits Name<-- #
# fruits1 = input("Write Fruit name 1: ")
# fruits2 = input("Write Fruit name 2: ")
# fruits3 = input("Write Fruit name 3: ")
# fruits4 = input("Write Fruit name 4: ")
# fruits5 = input("Write Fruit name 5: ")
# fruits = (fruits1, fruits2, fruits3, fruits4, fruits5)
# print(fruits)

# -->Sum of List<-- #
nums = [5, 1, 3, 4, 1, 1]
print(nums[0]+nums[1]+nums[2]+nums[3]+nums[4]+nums[5])
print(sum(nums))
print(nums.count(1))
