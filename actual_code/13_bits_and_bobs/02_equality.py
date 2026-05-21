import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(['red', 'green', 'blue'])

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1,2)

print(p1.x == p2.x and p1.y == p2.y)
print(p1 == p2)