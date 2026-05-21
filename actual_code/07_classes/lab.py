class Player:
  def __init__(self, name, guess_count=0, history=None):
    self.name = name
    self.guess_count = guess_count
    self.history = history if history is not None else []

  def __repr__(self):
    return f'Player(name={self.name}, guess_count={self.guess_count}, history={self.history})'

  def __str__(self):
    return f'Player(name={self.name}, guess_count={self.guess_count}, history={self.history})'

  def increment_count(self):
    self.guess_count += 1

  def add_guess(self, guess):
    self.history.append(guess)

  def print_history(self):
    for guess in self.history:
      print(guess)

  
class Game:
  def __init__(self):
    self.players = []
  
  def add_player(self, player):
    self.players.append(player)
  
  def play_game(self):
    for player in self.players:
      play_game(player)
  
  def print_results(self):
    for player in self.players:
      print(player)


# implement a guessing game using the Player class
# do it procedurally 

import random

MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = f'Please guess a number between {MIN_VALUE} and {MAX_VALUE}: '

def get_user_guess(prompt):
  return int(input(prompt))

def play_game(player):
  number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)
  guess = 0
  while number_to_guess != guess and player.guess_count != MAX_NUMBER_OF_GUESSES:
    guess = get_user_guess(GUESS_PROMPT)
    player.increment_count()
    player.add_guess(guess)
    if guess == -1:
      print(f'The number to guess is {number_to_guess}')
      break
    elif number_to_guess == guess:
      print('Correct Guess')
      break
    elif guess < number_to_guess:
      print('Sorry wrong number')
      print('Your guess was lower than the number')
    elif guess > number_to_guess:
      print('Sorry wrong number')
      print('Your guess was higher than the number')
  return player

players = []
while True:
  
  name = input('Enter your name: ')
  if name == '':
    break
  player = Player(name)
  player = play_game(player)
  players.append(player)

  play_again = input('Do you want to play again? (y/n): ')
  if play_again == 'n':
    break


for player in players:
  print(player)