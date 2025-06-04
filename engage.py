print("=== Student Engagement Assessment ===")

# Take input from user
try:
    questions_asked = int(input("Enter number of questions asked by the student: "))
    answers_shared = int(input("Enter number of answers shared by the student: "))
    sessions_attended = int(input("Enter number of sessions attended by the student: "))
    total_sessions = int(input("Enter total number of sessions conducted: "))

    # Basic validations
    if sessions_attended == 0 or total_sessions == 0:
        engagement_ratio = 0.0
        attendance_rate = 0.0
        assessment = "Insufficient Data"
    else:
        engagement_ratio = (questions_asked + answers_shared) / sessions_attended
        attendance_rate = sessions_attended / total_sessions

        if engagement_ratio > 0.7 and attendance_rate >= 0.6:
            assessment = "High Engagement"
        else:
            assessment = "Low Engagement"

    # Output results
    print("\n=== Result ===")
    print("Engagement Ratio:", round(engagement_ratio, 2))
    print("Attendance Rate:", round(attendance_rate, 2))
    print("Engagement Assessment:", assessment)

except ValueError:
    print("⚠️ Please enter valid integers for all inputs.")
