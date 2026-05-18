import random

# Set up some global 'constants'
MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = f'Please guess a number between {MIN_VALUE} and {MAX_VALUE}: '

# Set up variables to be used in the game
game_over = False

while not game_over:
    # Initialise the number to be guessed - includes both end points
    number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

    # Initialise the number of tries the player has made
    count_number_of_tries = 0

    # Start the game
    print('Welcome to the number guess game')

    # Obtain their initial guess
    while True:
        try:
            guess = int(input(GUESS_PROMPT))
        except ValueError:
            print('Please enter a whole number.')
            continue

        # Reveal/cheat without consuming a guess
        if guess == -1:
            print(f'The number to guess is {number_to_guess}')
            continue

        # Enforce range without consuming a guess
        if guess < MIN_VALUE or guess > MAX_VALUE:
            print(f'Out of range. Enter a number between {MIN_VALUE} and {MAX_VALUE}.')
            continue

        # A valid guess consumes a try
        count_number_of_tries += 1

        # Check win first
        if guess == number_to_guess:
            print('Well done you won!')
            print(f'You took {count_number_of_tries} goes to complete the game')
            break

        # Give feedback
        if abs(guess - number_to_guess) == 1:
            print('Sorry, wrong number - you were out by 1')
        elif guess < number_to_guess:
            print('Sorry, wrong number')
            print('Your guess was lower than the number')
        else:
            print('Sorry, wrong number')
            print('Your guess was higher than the number')

        # Out of guesses?
        if count_number_of_tries == MAX_NUMBER_OF_GUESSES:
            print("Sorry - you lose")
            print(f'The number you needed to guess was {number_to_guess}')
            break

    # Play again?
    while True:
        play_again = input("Do you want to play again (y/n) or (yes/no)? ").strip().lower()
        if play_again in ('n', 'no'):
            game_over = True
            break
        elif play_again in ('y', 'yes'):
            break
        else:
            print('Invalid input; must be y/n or yes/no')

print('Game Over')
    
