file = open("test.txt")

for line in file:
    print(line.strip())

file.close()

with open("test.txt") as file:
    for line in file:
        print(line.strip())