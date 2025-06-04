print("=== Student Doubt Clarification Assessment ===")

try:
    # Inputs
    student_doubts = int(input("Enter number of doubts asked by the student: "))
    avg_doubts = float(input("Enter average number of doubts in the class: "))

    # Validation
    if avg_doubts == 0:
        assessment = "Insufficient Data"
    else:
        # Categorization
        if student_doubts > avg_doubts * 1.25:
            assessment = "Highly Active Learner"
        elif student_doubts > avg_doubts:
            assessment = "Active Learner"
        elif student_doubts >= avg_doubts * 0.5:
            assessment = "Moderately Active"
        else:
            assessment = "Passive Learner"

    # Output
    print("\n=== Result ===")
    print("Student Doubts:", student_doubts)
    print("Class Average Doubts:", avg_doubts)
    print("Assessment:", assessment)

except ValueError:
    print("⚠️ Please enter valid numerical input.")
# This code assesses student engagement based on the number of doubts asked by the student compared to the class average.6
