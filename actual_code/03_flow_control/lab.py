import random

RANDOM_NUMBER = random.randint(1, 10)
number_of_guesses = 0
while number_of_guesses < 3:
    user_input = input("Enter a number: ")
    number_of_guesses += 1
    if not user_input.isdigit():
        print("Not a valid number.")
        continue
    user_input = int(user_input)

    if user_input == RANDOM_NUMBER:
        print("Correct!")
        break

    if user_input > RANDOM_NUMBER:
        print("Your number is too high!")
        continue

    if user_input < RANDOM_NUMBER:
        print("Your number is too low!")
        continue
else:
    print("You lost!")


