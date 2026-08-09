# Sample input data
students = [
    {"name": "chala", "score": 88},
    {"name": "diriba", "score": 92},
    {"name": "fayo", "score": 67},
    {"name": "sori", "score": 75},
]

# Configurable grade thresholds
GRADE_A_PLUS = 90
GRADE_A = 85
GRADE_A_MINUS= 80
GRADE_B_PLUS= 75
GRADE_B = 70
GRADE_B_MINUS = 65

GRADE_C_PLUS= 60
GRADE_C=50
GRADE_C_MINUS=45
GRADE_D = 40
GRADE_F = 0
total_score = 0
highest_score = float("-inf")
lowest_score = float("inf")
student_results = []

for student in students:
    name = student["name"]
    score = student["score"]

    # Determine letter grade using conditionals
    if score >= GRADE_A_PLUS:
        grade = "A+"
    elif score >= GRADE_A:
        grade = "A"
    elif score >= GRADE_A_MINUS:
        grade = "A-"
    elif score >= GRADE_B_PLUS:
        grade = "B+"
    elif score >= GRADE_B:
        grade = "B"
    elif score >= GRADE_B_MINUS:
        grade = "B-"
    elif score >= GRADE_C_PLUS:
        grade = "C+"
    elif score >= GRADE_C:
        grade = "C"
    elif score >= GRADE_C_MINUS:
        grade = "C-"
    elif score >= GRADE_D:
        grade = "D"
    else:
        grade = "F"

    # Track statistics
    total_score += score
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score

    # Store grade summary
    student_results.append({"name": name, "score": score, "grade": grade})
    num_students = len(students)
average_score = total_score / num_students if num_students > 0 else 0
print("--- INDIVIDUAL STUDENT GRADES ---")
for result in student_results:
    # String operations to format output
    print(f"Student: {result['name']:<10} | Score: {result['score']:<3} | Grade: {result['grade']}")

print("\n--- CLASS SUMMARY STATISTICS ---")
print(f"Total Students : {num_students}")
print(f"Average Score  : {average_score:.2f}")
print(f"Highest Score  : {highest_score}")
print(f"Lowest Score   : {lowest_score}")