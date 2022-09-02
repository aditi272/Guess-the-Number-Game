import random
import art
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
attempts_easy = 10
attempts_hard = 5
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
rand = random.randint(1,100)
# print(f"Psssst, the correct number is {rand}")

choose_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")

if choose_level == 'easy':
  over = False
  print('You have 10 attempts remaining to guess the number.')
  while not over:
    if attempts_easy > 0:
      make_a_guess = int(input("Make a guess: "))
      if make_a_guess != rand:
        if make_a_guess > rand:
          print("Too High.")
          
        else:
          print("Too Low.")
        
        attempts_easy = attempts_easy -1
        if attempts_easy > 0:
          print('Try again.')
          print(f"You have {attempts_easy} attempts remaining to guess the number.")
        
      else:
        print(f"You got it the answer was {make_a_guess}.")
        over = True
    else:
      print("You have run out of guesses, you lose")
      over = True
elif choose_level == 'hard':
  over = False
  print('You have 5 attempts remaining to guess the number.')
  while not over:
    if attempts_hard > 0:
      make_a_guess = int(input("Make a guess: "))
      if make_a_guess != rand:
        if make_a_guess > rand:
          print("Too High.")
          
        else:
          print("Too Low.")
        
        attempts_hard = attempts_hard -1
        if attempts_hard > 0:
          print('Try again.')
          print(f"You have {attempts_hard} attempts remaining to guess the number.")
        
      else:
        print(f"You got it the answer was {make_a_guess}.")
        over = True
    else:
      print("You have run out of guesses, you lose")
      over = True
else:
  print("Invalid Run Again!")
  
  

  
  
  