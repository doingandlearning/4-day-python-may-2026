for i in range(10):  # 0 - 9
    print("Hello and good morning - isn't Python great!")

coord = [(1,2,5), (3,4,7), (5,6,7)] # Know the shape of the data!

for item in coord:
    print(item)
    print(f"The x-ordinate is {item[0]}")
    print(f"The y-ordinate is {item[1]}")

for x, y, _ in coord:
    print(x,y)
    print(f"The x-ordinate is {x}")
    print(f"The y-ordinate is {y}")

for item in enumerate(coord):
    print(f"The {item[0]}-ordinate is {item[1]}")

for i in range(len(coord)):
    print(coord[i])