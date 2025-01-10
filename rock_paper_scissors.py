import random

def get_computer_choice():
  """
  Get computer choice using random.choice
  """
  options = ('rock','paper','scissors')
  computer_choice = random.choice(options)
  return computer_choice
  
def get_user_choice():
  """
  get user input
  """
  options = ('rock','paper','scissors','q')
  user_choice = input("Enter Rock, Paper or Scissors (or 'q' to quit): ").lower()
  while user_choice not in options:
    user_choice = input("Invalid input\nEnter rock paper, scissors: ")
  return user_choice
  
  
def determine_winner(user_choice,computer_choice):
  
  if user_choice == computer_choice:
    return "It's a tie"
  elif (user_choice == "rock" and computer_choice=="paper") or \
       (user_choice == "scissors" and computer_choice== "paper") or \
      (user_choice == "paper" and computer_choice == "rock"):
        return "You won!!!"
  else:
    return "Computer Wins!!!"
        
  
def play_game():
  while True:
    user_choice = get_user_choice()
    if user_choice == "q":
      print("Good bye")
    else:  
      computer_choice = get_computer_choice()
      print(f"You choosed {user_choice}, the computer choosed {computer_choice}\n")
      winner = determine_winner(user_choice, computer_choice)
      print(winner)
  

play_game()
    