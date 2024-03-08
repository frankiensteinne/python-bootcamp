year = int(input("Input year: "))
isLeap = True

if year % 4 == 0:
  isLeap
  if year %100 == 0:
    isLeap = False
    if year % 400 == 0:
      isLeap = True
else:
    isLeap = False

if isLeap:
   print(f"{year} is a leap year!")
else:
   print(f"{year} is not a leap year.")