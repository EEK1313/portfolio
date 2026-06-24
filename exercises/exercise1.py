def calculate_grade(assignments, midterm, final):
    assignment_avg = sum(assignments) / len(assignments)

    overall_grade = (
        assignment_avg * 0.20 +
        midterm * 0.30 +
        final * 0.50
    )

    if overall_grade >= 90:
        letter_grade = "A"
    elif overall_grade >= 80:
        letter_grade = "B"
    elif overall_grade >= 70:
        letter_grade = "C"
    elif overall_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    return overall_grade, letter_grade


assignments = [85, 90, 78, 92]
midterm = 80
final = 88

grade, letter = calculate_grade(assignments, midterm, final)

print(f"Final Grade: {grade:.2f}")
print(f"Letter Grade: {letter}")
