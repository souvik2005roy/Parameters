print("=== 🧭 Navigation Behavior Assessment ===")

try:
    print("\n🔹 Rate the following between 0.0 (low) and 2.0 (high):")

    sequential_solving = float(input("1. Logical/Sequential Solving (0 = random, 2 = linear): "))
    revisits = float(input("2. Revisits previous questions appropriately: "))
    skips = float(input("3. Leaves questions unattempted/skips without returning (0 = many skips, 2 = none): "))

    if any(x < 0.0 or x > 2.0 for x in [sequential_solving, revisits, skips]):
        print("⚠️ Please enter values between 0.0 and 2.0 only.")
    else:
        total_score = sequential_solving + revisits + skips

        if total_score >= 5:
            assessment = "🧭 Strategic and Focused Navigator"
        elif total_score >= 3:
            assessment = "⚠️ Partial or Inconsistent Navigation"
        else:
            assessment = "🚨 Poor Navigation Behavior"

        print("\n=== 📋 NAVIGATION BEHAVIOR REPORT ===")
        print(f"Sequential Solving: {sequential_solving}")
        print(f"Revisits: {revisits}")
        print(f"Skips Score: {skips}")
        print(f"Total Navigation Score: {total_score:.2f} / 6.00")
        print("Assessment:", assessment)

except ValueError:
    print("⚠️ Please enter valid decimal numbers between 0.0 and 2.0.")
# This code assesses a student's navigation behavior based on their input scores.