print("=== 🎯 Accuracy + Time Efficiency Assessment ===")

try:
    attempted = int(input("Total questions attempted: "))
    correct = int(input("Correct answers: "))
    avg_time = float(input("Average time per question (in seconds): "))
    ideal_time = float(input("Ideal avg time per question (e.g. 60s): "))
    confidence = float(input("Self-rated confidence (0.0 to 2.0): "))

    if attempted == 0:
        print("⚠️ Cannot calculate accuracy. Attempted = 0.")
    else:
        accuracy = (correct / attempted) * 100
        time_efficiency = avg_time <= ideal_time

        # Base accuracy label
        if accuracy >= 80:
            if time_efficiency:
                label = "✅ Highly Efficient & Accurate"
            else:
                label = "🧠 Accurate but Needs Speed"
        elif accuracy >= 50:
            if time_efficiency:
                label = "⚠️ Fast but Inaccurate"
            else:
                label = "❌ Inaccurate and Slow"
        else:
            label = "🚨 Needs Conceptual Reinforcement"

        # Output
        print("\n=== 📋 ACCURACY + TIME REPORT ===")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Average Time per Question: {avg_time:.2f}s (Ideal: {ideal_time}s)")
        print(f"Confidence Score: {confidence}")
        print("Assessment:", label)

except ValueError:
    print("⚠️ Enter valid numeric values only.")
# This code assesses a student's accuracy and time efficiency based on their input data.
# It calculates accuracy percentage, checks time efficiency against an ideal time, and provides a label based on performance.