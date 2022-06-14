class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()
point1.x = 100
print(point1.x)
point1.draw()
point1.move()

point2 = Point()
point2.y = 200
print(point2.y)
point2.move()
point2.draw()
