quiz = []

for i in range(1, 6):
    quizzes = int(input(f"{i} Enter your quiz grade: "))
    quiz.append(quizzes)

average = sum(quiz)/len(quiz)
total = sum(quiz)
highest = max(quiz)
lowest = min(quiz)
ascending = sorted(quiz)
descending = ascending[::-1]


print(f"Quiz: {quiz}")
print(f"Number of quizzes: {len(quiz)}")
print(f"Total score: {total}")
print(f"Average grade: {average:.2f}")
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")
print(f"Ascending: {ascending}")
print(f"Descending: {descending}")
print(f"Original scores: {quiz}")