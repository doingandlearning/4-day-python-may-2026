class Vector:
    def __init__(self, x, y):
        if x == 0 and y == 0:
            raise ValueError("Can't have a zero vector")
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(1,2)

v3 = v1 + v2
print(v3.x, v3.y)

a = 3
b = 5
print(a + b)

# pandas
# matplotlib
