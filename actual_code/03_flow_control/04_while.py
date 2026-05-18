SECRET = "password123"
number_of_attempts = 0
user_input = None

while SECRET != user_input and number_of_attempts < 3:
    user_input = input("Enter your password: ")
    if user_input == SECRET:
        continue
    print("Incorrect password.")
    number_of_attempts += 1

if number_of_attempts < 3:
    print("Here are you secret documents")