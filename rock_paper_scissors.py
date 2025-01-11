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
# 0 rock, 1 paper , 2 scissors
import random
computer_choice = random.randint(0,2)
computer_icon = ""
if computer_choice == 0:
    computer_icon=rock
elif computer_choice == 1:
    computer_icon=paper
else:
    computer_icon=scissors
user_choice = int(input("Welcome to the game\nPlease choose, 0 For rock, 1 For Paper or 2 for scissors: "))
if user_choice == 0 or user_choice == 1 or user_choice ==2 :
    user_icon = ""
    if user_choice == 0:
        user_icon=rock
    elif user_choice == 1:
        user_icon=paper
    elif user_choice == 2:
        user_icon=scissors
    print("Your Choice:")
    print(user_icon)
    print("Computer Choice:")
    print(computer_icon)
    if computer_choice == user_choice:
       print("Its Draw")
    else:
        if user_choice == 0 and computer_choice ==1:
            print("Computer win")
        elif user_choice == 0 and computer_choice ==2:
            print("User win")
        elif user_choice == 1 and computer_choice ==0:
            print("User win")
        elif user_choice == 1 and computer_choice ==2:
            print("Computer win")
        elif user_choice == 2 and computer_choice ==0:
            print("Computer win")
        else:
            print("User win")
else:
    print("you lose, you chose wrong number")
