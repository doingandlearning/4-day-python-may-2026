is_teenager = None
age = 15

if age < 20 and age > 12:
    is_teenager = True
else:
    is_teenager = False

print(is_teenager)

is_teenager = True if 12 < age < 20 else False
print(is_teenager)