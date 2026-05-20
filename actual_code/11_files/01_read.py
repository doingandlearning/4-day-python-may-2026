file = open("test.txt")

contents = file.read()
print(contents)
print(type(contents))

print(file.tell())
file.seek(0)
print(file.tell())

contents = file.readlines()
print(contents)
print(type(contents))

for line in contents:
    print(line.strip())

file.seek(0)
print("=" * 100)
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()

file.seek(0)

for line in file:
    print(line.strip())

file.close()