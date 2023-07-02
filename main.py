from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5
 
# function to check user number to the actual number 
def check_answer(guess,answer,turns):
  """Checks the answer and returns the number of turns left."""
  if guess > answer:
    print("Too high.")
    return turns -1 
  elif guess < answer:
    print("Too low.")
    return turns -1
  else:
    print(f"You got it!! The answer is {answer}.")


# function to set difficulty level
def set_diffculty():
  level = input("Choose a diffculty level. Type 'easy' or 'hard'.")
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL 
    
def game():    
  #chosing a number and starting text 
  print("WELCOME TO THE NUMBER GUESSING GAME!!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100)
  turns = set_diffculty()
  
  # repeat the guessing function until the turns are over or if the guess is wrong 
  guess = 0
  while guess!= answer:
    print(f"You have {turns} attempts left to guess the number.")
  # guessing a number 
    guess = int(input("Make a guess "))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You've run out of move. You lose :(")
      return 
    elif guess != answer:
      print("Guess again")
# track the number of chances and reduce it by one 
game()

