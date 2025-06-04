import pandas as pd
import matplotlib.pyplot as plt

# Ask for number of chapters
num_chapters = int(input("📘 How many chapters do you want to enter? "))

# Initialize lists
chapters = []
correct = []
incorrect = []
skipped = []

# Input loop
print("\n📥 Enter chapter names and your performance data:")
for i in range(num_chapters):
    name = input(f"\n📗 Chapter {i+1} name: ").strip()
    c = int(input(f"✅ Correct answers in {name}: "))
    i_ = int(input(f"❌ Incorrect answers in {name}: "))
    s = int(input(f"⏭️ Skipped questions in {name}: "))
    chapters.append(name)
    correct.append(c)
    incorrect.append(i_)
    skipped.append(s)

# Build DataFrame
df = pd.DataFrame({
    "Chapter": chapters,
    "Correct": correct,
    "Incorrect": incorrect,
    "Skipped": skipped
})

df["Total"] = df["Correct"] + df["Incorrect"] + df["Skipped"]
df["Weak Attempts"] = df["Incorrect"] + df["Skipped"]
df["Gap %"] = (df["Weak Attempts"] / df["Total"]) * 100
df.sort_values(by="Gap %", ascending=False, inplace=True)

# Plotting
plt.figure(figsize=(13, 6))
colors = ["red" if x > 60 else "orange" if x > 40 else "green" for x in df["Gap %"]]
bars = plt.barh(df["Chapter"], df["Gap %"], color=colors)
plt.title("📘 Chapters That Need Your Attention", fontsize=16)
plt.xlabel("Learning Gap (%)", fontsize=12)
plt.xlim(0, 100)
plt.gca().invert_yaxis()

for bar, gap in zip(bars, df["Gap %"]):
    msg = "🚨 High Priority" if gap > 60 else "⚠️ Needs Work" if gap > 40 else "✅ Doing Well"
    plt.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2,
             f"{gap:.1f}% - {msg}", va='center', fontsize=9)

plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# Print suggestions
weakest = df[df["Gap %"] > 60]
if not weakest.empty:
    print("\n🔔 Focus first on these chapters (High Priority):")
    for chap in weakest["Chapter"]:
        print(f"➡️ {chap}")
else:
    print("\n✅ No major weak chapters. Focus on these for improvement:")
    for chap in df[df["Gap %"] > 40]["Chapter"]:
        print(f"➡️ {chap}")
