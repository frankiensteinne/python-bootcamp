print("Welcome to Pizza Ponzi")
size = input("What size do you want? S, M, or L\n")
add_pepperoni = input("Do you want Pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

total = 0

if (size == "L" or size == "M") and add_pepperoni == "Y":
    total += 3
if size == "S" and add_pepperoni == "Y":
    total += 2
if extra_cheese == "Y":
    total += 1
if size == "S":
    total += 15
if size == "M":
    total += 20
if size =="L":
    total += 25

print(f"Thanks for choosing Pizza Ponzi, your final bill is PhP {total}.")
