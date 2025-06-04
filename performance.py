import matplotlib.pyplot as plt

# Take user input for 5 tests
tests = ["Test 1", "Test 2", "Test 3", "Test 4", "Test 5"]
scores = []
engagement = []
confidence = []
accuracy = []
attempted = []
improvement_speed = []

print("📥 Enter performance data for 5 tests:\n")

for i in range(5):
    print(f"\n{tests[i]}:")
    scores.append(float(input("→ Score (%): ")))
    engagement.append(float(input("→ Engagement Ratio (0-1): ")))
    confidence.append(float(input("→ Concept Confidence (0-1): ")))
    accuracy.append(float(input("→ Accuracy (0-1): ")))
    attempted.append(float(input("→ Questions Attempted % (0-1): ")))
    improvement_speed.append(float(input("→ Improvement Speed (e.g., 1.3): ")))

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))
fig.suptitle("📊 Consolidated Student Performance Metrics", fontsize=16)

# Primary Axis: Score
ax1.plot(tests, scores, color="blue", marker="o", label="Score (%)")
ax1.set_ylabel("Score (%)", color="blue")
ax1.tick_params(axis='y', labelcolor="blue")
ax1.set_ylim(0, 100)

# Secondary Axis: Ratios
ax2 = ax1.twinx()
ax2.plot(tests, engagement, color="purple", marker="x", linestyle="--", label="Engagement Ratio")
ax2.plot(tests, confidence, color="green", marker="s", linestyle="--", label="Concept Confidence")
ax2.plot(tests, accuracy, color="orange", marker="d", linestyle="--", label="Accuracy")
ax2.plot(tests, attempted, color="red", marker="^", linestyle="--", label="Questions Attempted %")
ax2.set_ylabel("Ratio / Percentage", color="gray")
ax2.tick_params(axis='y', labelcolor="gray")
ax2.set_ylim(0, 1.1)

# Improvement speed annotations
for i, val in enumerate(improvement_speed):
    ax1.annotate(f"↑{val}", (i, scores[i] + 2), color="blue", fontsize=9, ha='center')

# Combined Legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9)

# Explanatory text
description = (
    "Legend:\n"
    "🔹 Score: Test score out of 100\n"
    "🟣 Engagement: Participation in learning (0–1)\n"
    "🟢 Confidence: Conceptual clarity (0–1)\n"
    "🟠 Accuracy: Correctness of attempts (0–1)\n"
    "🔴 Attempted %: Proportion of questions attempted\n"
    "⬆ Speed: Rate of improvement between tests"
)
plt.gcf().text(1.02, 0.5, description, fontsize=10, va='center', ha='left', bbox=dict(facecolor='white', edgecolor='gray'))

plt.tight_layout()
plt.show()
