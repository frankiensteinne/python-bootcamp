student_scores = [92, 89, 93, 84,95, 88, 97, 99, 91, 82]
highest_score = 0

for score in student_scores:
    score = int(score)
    if score > highest_score:
        highest_score = score
        print(highest_score)

print("Final",highest_score)



