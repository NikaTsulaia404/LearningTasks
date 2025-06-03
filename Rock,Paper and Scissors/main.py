import random
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random

archeva = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if archeva not in (0, 1, 2):
    print("Error! Please choose 0, 1 or 2.")
else:
    kompis_archevani = random.randint(0, 2)
    print(f"Computer choice: {kompis_archevani}")

    if archeva == 0 and kompis_archevani == 2:
        print("User wins!")
    elif archeva == 1 and kompis_archevani == 0:
        print("User wins!")
    elif archeva == 2 and kompis_archevani == 1:
        print("User wins!")
    elif archeva == kompis_archevani:
        print("Draw!")
    else:
        print("Computer wins!")

