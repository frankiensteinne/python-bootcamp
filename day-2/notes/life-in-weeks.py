maxWeeks = 90 * 52
yourAge = int(input("How old are you in years?:\n"))

yourAgeWeeks = yourAge * 52
leftWeeks = maxWeeks - yourAgeWeeks

print(f"You have {leftWeeks} weeks left")