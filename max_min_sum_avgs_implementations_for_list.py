student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
min_score = student_scores[0]
max_score = student_scores[0]
sum_score = 0
for score in student_scores:
    sum_score += score
    if min_score > score:
        min_score   = score
    if max_score < score:
        max_score = score
avg_score = sum_score / len(student_scores)

print(f"Sum is: {sum_score}")
print(sum(student_scores))
print(f"Avg is: {avg_score}")
print(f"Min is: {min_score}")
print(min(student_scores))
print(f"Max is: {max_score}")
print(max(student_scores))
