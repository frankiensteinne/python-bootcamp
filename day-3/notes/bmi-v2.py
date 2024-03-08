weight = int(input("What is your weight in kilogram?\n"))
height = float(input("What is your height meters?\n"))

bmi = weight / height**2
message = f"Your BMI is {bmi}."

if bmi < 18.5:
    print(f"{message} You are underweight.")
elif 18.5 <= bmi < 25:
    print(f"{message} You have a normal weight.")
elif 25 <= bmi < 30:
    print(f"{message} You are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"{message} You are obese")
else:
    print(f"{message} You are clinically obese.")
