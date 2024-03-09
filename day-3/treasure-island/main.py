from art import treasure

# Initial game state
game_over = False

print("Welcome to treasure island. Your mission is to find the treasure!")

# First choice: Left or Right
first_choice = input("Choose where to go: Left or Right?\n").lower()  # Case-insensitive choice
if first_choice != "left":
    game_over = True

# Second choice (only if first choice was correct)
if not game_over:
    second_choice = input("Choose what to do: Swim or Wait?\n").lower()
    if second_choice != "wait":
        game_over = True

# Third choice (only if both previous choices were correct)
if not game_over:
    third_choice = input("Choose a door: Red, Yellow, or Blue?\n").lower()
    if third_choice != "blue":
        game_over = True
    else:  # All choices were correct
        print("You win!")
        print(treasure)  

# Print "Game Over!" based on game state
if game_over:
    print("Game Over!")
