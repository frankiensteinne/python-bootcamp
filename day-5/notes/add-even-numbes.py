sum = 0

ceiling_num = int(input("Input Number: "))
ceiling_num += 1

for numbers in range(0,ceiling_num,2):
    sum += numbers

print(sum)