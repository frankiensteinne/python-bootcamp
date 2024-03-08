# Welcome Message
print("Welcome to the tip calculator!")

# Get total bill
total =  float(input("What is your total bill?: PhP "))

# Get tip percentage
tipPercentage =  int(input("How much tip would you like to give? 10, 12, or 15? "))

# How many pax?
pax = int(input("How many people will split the bill? "))

# Computing for the tip
tip = round((total + (total * (tipPercentage/100)))/pax, 2)

# Showing Tip Total
print(f"Each person should pay Php {tip}.")

