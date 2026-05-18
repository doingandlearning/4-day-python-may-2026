first_v = None
second_v = None

print(first_v == second_v)
print(first_v == None)
print(first_v is None)

first_v = "hello" * 1000
second_v = "hello" * 1000

print(first_v == second_v)
print(first_v is second_v)