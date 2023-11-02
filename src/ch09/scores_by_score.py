
scores = {}

with open("testscores.dat") as scores_in:

    for line in scores_in:
        name, score = line.split(":")
        score = int(score)
        scores[name] = score

for student, score in sorted(scores.items(), key=lambda e: (e[1]), reverse=True):
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'

    print(f"{student} {score} {grade}")

sumOfScores = sum(scores.values())
average = sumOfScores/len(scores)
print()
print(f"average score is {average:.2f}")
