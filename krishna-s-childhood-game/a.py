import random

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

game_images = [rock, paper, scissors]

while True:
    user_choice = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, or any other number to exit.\n"))
    if user_choice < 0 or user_choice > 2:
        print("Exiting the game.")
        break

    print("You chose:")
    print(game_images[user_choice])

    krishna_choice = random.randint(0, 2)
    print("Krishna's choice:")
    print(game_images[krishna_choice])

    if user_choice == krishna_choice:
        print("It's a tie!")
    elif (user_choice == 0 and krishna_choice == 2) or \
            (user_choice == 1 and krishna_choice == 0) or \
            (user_choice == 2 and krishna_choice == 1):
        print("You win!")
    else:
        print("Krishna wins!")

    print("\nLet's play again!\n")
