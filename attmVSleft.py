print("=== 📚 Concept Coverage & Attempt Ratio Assessment ===")

try:
    total_questions = int(input("Total number of questions assigned: "))
    attempted_questions = int(input("Number of questions attempted: "))
    clarity = float(input("Self-rated concept clarity (0.0–2.0): "))
    days_left = int(input("Number of days left for the exam: "))

    if total_questions == 0:
        print("⚠️ Cannot compute. Total questions cannot be zero.")
    else:
        attempt_ratio = (attempted_questions / total_questions) * 100

        if attempt_ratio < 50 and clarity < 1.0 and days_left < 7:
            label = "🚨 Alarming: Very Low Coverage and Clarity"
        elif attempt_ratio < 80 and clarity < 1.5:
            label = "⚠️ Needs Immediate Focus and Revision"
        elif attempt_ratio >= 80 and clarity >= 1.5:
            label = "✅ Well Prepared and Conceptually Clear"
        else:
            label = "🟡 Moderate Preparation – Keep Tracking Progress"

        print("\n=== 📋 COVERAGE REPORT ===")
        print(f"Attempted: {attempted_questions} / {total_questions} → {attempt_ratio:.2f}%")
        print(f"Concept Clarity: {clarity}/2.0")
        print(f"Days Left: {days_left}")
        print("Assessment:", label)

except ValueError:
    print("⚠️ Please enter valid numeric values only.")
