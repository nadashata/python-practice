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
choice_image=[rock, paper, scissors]
import random
computer_choice = random.randint(0,2)
user_choice = int(input("Welcome to the game\nPlease choose, 0 For rock, 1 For Paper or 2 for scissors: "))
if user_choice == 0 or user_choice == 1 or user_choice ==2 :
    print(f"Your Choice:\n{choice_image[user_choice]}")
    print(f"Computer Choice:\n{choice_image[computer_choice]}")
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
