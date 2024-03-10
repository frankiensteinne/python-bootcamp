import random

# List of available plays
sps = ["Rock", "Paper", "Scissors"]

# Turn input into integer so logical operators will run and not throw an error back.
player_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

# Eliminate the impossible plays / inputs
if player_choice > len(sps)-1 or 0 > player_choice:
    print("Please choose a valid number.")
    
# Run game logic if player input is valid
else:
    computer_choice = random.randint(0, len(sps)-1)
    generic_message = f"Computer picks {sps[computer_choice]}, you choose {sps[player_choice]}."
        
    if computer_choice == player_choice:
        print(generic_message + "It's a tie.")
    elif (computer_choice == 0 and player_choice == 1) or (computer_choice == 1 and player_choice == 2) or (computer_choice == 2 and player_choice == 0):
        print(generic_message + "You win!")
    else:
        print(generic_message + "You lose.")