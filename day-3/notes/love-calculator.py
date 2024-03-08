yourName = input("What is your name?\n")
theirName = input("What is their name?\n")

combinedNames = yourName + theirName
lowercased = combinedNames.lower()

t = lowercased.count("t")
r = lowercased.count("r")
u = lowercased.count("u")
e = lowercased.count("e")

firstDigit = t + r + u + e

l = lowercased.count("l")
o = lowercased.count("o")
v = lowercased.count("v")

secondDigit = l + o + v + e

loveScore = int(str(firstDigit)+str(secondDigit))
genericMessage = f"Your love score is {loveScore}"

if loveScore < 10 or loveScore > 90:
    print(f"{genericMessage}, you go together like coke and mentos.")
elif 40 < loveScore < 50:
    print(f"{genericMessage}, you are alright together.")
else:
    print(genericMessage + ".")