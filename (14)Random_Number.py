import random

# for i in range(5):
#     print(random.randint(10, 20))

# members = ['Nasif', 'Azam', 'Zisha', 'Jarin']
# print(random.choice(members))


# class Dice:
#     def roll(self):
#         num = (1, 2, 3, 4, 5, 6)
#         for i in num:
#             print(f"({random.choice(num)}, {random.choice(num)})")


# Dice.roll()

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
