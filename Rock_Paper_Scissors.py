# Straight forward Rock/Paper/Scissors with some provided art from the course.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0,2)
print(game_images[user_choice])
print("Computer chose:")
print(computer_choice)
print(game_images[computer_choice])
if user_choice >2 or user_choice <0:
  print("You typed an invalid number, you lose!")
elif user_choice == computer_choice:
  print("It's a draw")
elif user_choice == 0 and computer_choice == 1:
  print("You lose")
elif user_choice == 1 and computer_choice == 2:
  print("You lose")
elif user_choice == 2 and computer_choice == 0:
  print("You lose")
else:
  print("You win")