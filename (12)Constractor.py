# Contractor
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("Move")

#     def draw(self):
#         print("Draw")


# point = Point(10, 20)
# point.x = 5000
# print(point.x, point.y)

class Person:
    def __init__(self, name):  # Constractor
        self.name = name

    def talk(self):
        print(f"Hi!! It's {self.name}")


person_nasif = Person("Nasif Azam")
person_zisha = Person("Jarin Zisha")
person_shakt = Person("Shakt Launda")
# print(person_nasif.name)
# print(person_zisha.name)
# print(person_shakt.name)
person_nasif.talk()
person_zisha.talk()
person_shakt.talk()
