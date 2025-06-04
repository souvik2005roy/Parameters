print("=== Student Attendance Assessment ===")

try:
    # Input from user
    sessions_attended = int(input("Enter number of sessions attended by the student: "))
    total_sessions = int(input("Enter total number of sessions conducted: "))

    # Validation and calculation
    if total_sessions == 0:
        attendance_rate = 0.0
        assessment = "Insufficient Data"
    else:
        attendance_rate = sessions_attended / total_sessions

        # Categorize based on rate
        if attendance_rate >= 0.9:
            assessment = "Excellent Attendance"
        elif attendance_rate >= 0.75:
            assessment = "Regular Attendance"
        elif attendance_rate >= 0.6:
            assessment = "Needs Improvement"
        else:
            assessment = "Irregular Attendance"

    # Output
    print("\n=== Result ===")
    print("Attendance Rate:", round(attendance_rate, 2))
    print("Attendance Assessment:", assessment)

except ValueError:
    print("⚠️ Please enter valid integers.")
# This code assesses student attendance based on the number of sessions attended and total sessions conducted.
# It categorizes attendance into four levels: Excellent, Regular, Needs Improvement, and Irregular.