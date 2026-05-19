empty_list = []
empty_list = list()


beatles_list = ["John", "Paul", "Ringo", "George", "Ringo", "Ringo"]
# Slice! []
print("John" in beatles_list) # check for membershpi

for beatle in beatles_list: # loop
    print(beatle)

# .count() and index() and unpack

# CRUD
# Create
beatles_list.append("Leonardo")  # single item
print(beatles_list)

beatles_list.extend(["Sheik", "Alfredo"])
print(beatles_list)

beatles_list.insert(1, "Jon")
print(beatles_list)

# Read
print(beatles_list[0])

print(beatles_list.pop())
print(beatles_list)


# Update
beatles_list[0] = "Marko"
print(beatles_list)

# Delete
while "Ringo" in beatles_list:
    beatles_list.remove("Ringo")
print(beatles_list)

del beatles_list[0]
print(beatles_list)

del beatles_list[3:]
print(beatles_list)

# .sort
print(sorted(beatles_list))


new_beatles = beatles_list.copy()
print(beatles_list)
print(new_beatles)

new_beatles.append("Ringo")
print(new_beatles)
print(beatles_list)
print(new_beatles is beatles_list)

print(tuple(sorted((4,3,1))))

test = [1,2,3]
test = test + [4,5,6]
print(test)
