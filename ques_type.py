question_types = ["MCQ", "Short Answer", "Numerical", "Long Answer"]

results = []

print("=== ❓ Question Type Preference Evaluation ===")

for q_type in question_types:
    print(f"\n--- {q_type} ---")
    total = int(input(f"Total {q_type} questions given: "))
    attempted = int(input(f"{q_type} questions attempted: "))
    correct = int(input(f"{q_type} questions correct: "))

    if total == 0 or attempted == 0:
        attempt_rate = 0
        accuracy = 0
    else:
        attempt_rate = (attempted / total) * 100
        accuracy = (correct / attempted) * 100 if attempted > 0 else 0

    # Preference logic
    if attempt_rate >= 70 and accuracy >= 70:
        label = "✅ Preferred & Mastered"
    elif attempt_rate < 40 and accuracy < 50:
        label = "🚫 Avoided or Unconfident"
    elif attempt_rate >= 60 and accuracy < 60:
        label = "⚠️ Tried but Needs Clarity"
    elif attempt_rate < 40 and accuracy >= 70:
        label = "🟡 Knows it but Avoids"
    else:
        label = "🟢 Neutral"

    results.append({
        "Type": q_type,
        "Attempt Rate (%)": round(attempt_rate, 2),
        "Accuracy (%)": round(accuracy, 2),
        "Assessment": label
    })

# Display result
import pandas as pd
df_result = pd.DataFrame(results)
print("\n=== 📋 Question Type Report ===")
print(df_result.to_string(index=False))
