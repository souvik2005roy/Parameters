import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# === Get user input ===
num_chapters = int(input("Enter the number of chapters: "))

chapters = []
total_qs = []
wrong_qs = []
skipped_qs = []

for i in range(num_chapters):
    print(f"\n--- Chapter {i+1} ---")
    ch_name = input("Chapter name: ")
    total = int(input("Total questions: "))
    wrong = int(input("Wrong answers: "))
    skipped = int(input("Skipped questions: "))

    # Validation
    if wrong + skipped > total:
        print("⚠️ Wrong + Skipped cannot exceed Total. Try again.")
        continue

    chapters.append(ch_name)
    total_qs.append(total)
    wrong_qs.append(wrong)
    skipped_qs.append(skipped)

# === Build DataFrame ===
df = pd.DataFrame({
    "Chapter": chapters,
    "Total Qs": total_qs,
    "Wrong Qs": wrong_qs,
    "Skipped Qs": skipped_qs
})

# === Assessment logic ===
labels = []
for i in range(len(df)):
    total = df["Total Qs"][i]
    wrong = df["Wrong Qs"][i]
    skipped = df["Skipped Qs"][i]

    if wrong >= total * 0.5:
        label = "❌ High Mistakes – Poor Understanding"
    elif skipped >= total * 0.5:
        label = "⏭️ Avoided – Needs Review"
    elif wrong + skipped <= total * 0.2:
        label = "✅ Well Prepared"
    else:
        label = "🟡 Moderate Attention Needed"

    labels.append(label)

df["Assessment"] = labels

# === Plot 1: Grouped Bar Chart ===
fig1, ax1 = plt.subplots(figsize=(10, 5))
x = np.arange(len(df["Chapter"]))
width = 0.35

ax1.bar(x - width/2, df["Wrong Qs"], width, label='Wrong Answers', color='crimson')
ax1.bar(x + width/2, df["Skipped Qs"], width, label='Skipped Questions', color='steelblue')

ax1.set_xticks(x)
ax1.set_xticklabels(df["Chapter"])
ax1.set_ylabel("Count")
ax1.set_title("Chapter-wise Wrong vs Skipped Questions")
ax1.legend()
plt.tight_layout()
plt.show()

# === Plot 2: Stacked Bar Chart ===
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(df["Chapter"], df["Wrong Qs"], label='Wrong', color='salmon')
ax2.bar(df["Chapter"], df["Skipped Qs"], bottom=df["Wrong Qs"], label='Skipped', color='lightblue')
ax2.bar(
    df["Chapter"],
    df["Total Qs"] - df["Wrong Qs"] - df["Skipped Qs"],
    bottom=df["Wrong Qs"] + df["Skipped Qs"],
    label='Correct',
    color='lightgreen'
)

ax2.set_ylabel("Total Questions")
ax2.set_title("Question Distribution by Chapter")
ax2.legend()
plt.tight_layout()
plt.show()

# === Final Report Table ===
print("\n=== 📋 Chapter-wise Diagnostic Report ===")
print(df.to_string(index=False))
