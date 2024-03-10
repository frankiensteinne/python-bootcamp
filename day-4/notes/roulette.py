import random

names = ["Bobby", "Lisa", "Mary", "John", "Jane"]

max_num = len(names)
index = random.randint(0, max_num-1)

print(f"{names[index]} will foot this bill.")
