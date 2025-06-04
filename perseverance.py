print("=== 💪 Perseverance & Retry Effort Assessment (with decimals) ===")

try:
    print("\n🔹 Enter a score between 0.0 and 2.0 (you can use decimals like 1.5)")

    retry_rate = float(input("1. Retry rate (e.g. 0.0 = rarely retries, 2.0 = retries often): "))
    retry_time = float(input("2. Avg. time spent per retry (e.g. 0.0 = <30s, 2.0 = >90s): "))
    retry_success = float(input("3. Success rate after retry (e.g. 0.0 = <40%, 2.0 = >70%): "))

    if any(x < 0 or x > 2 for x in [retry_rate, retry_time, retry_success]):
        print("⚠️ Please enter values between 0.0 and 2.0 only.")
    else:
        total_score = retry_rate + retry_time + retry_success

        if total_score >= 5.0:
            assessment = "Highly Perseverant and Reflective"
        elif total_score >= 3.0:
            assessment = "Moderate Effort & Perseverance"
        elif total_score >= 1.0:
            assessment = "Low Perseverance or Surface Attempts"
        else:
            assessment = "Avoidant or Passive Learner"

        print("\n=== 📋 PERSEVERANCE RESULT ===")
        print(f"Retry Rate: {retry_rate}, Retry Time: {retry_time}, Retry Success: {retry_success}")
        print("Total Score: {0:.2f} / 6.00".format(total_score))
        print("Assessment:", assessment)

except ValueError:
    print("⚠️ Invalid input. Please enter decimal values (e.g. 1.5, 2.0)")
# This code assesses a student's perseverance and retry effort based on their input scores.