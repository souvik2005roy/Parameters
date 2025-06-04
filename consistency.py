import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from statistics import stdev

# --- User Input ---
try:
    total_chapters = int(input("Enter total number of chapters: "))

    print(f"\nEnter number of attempts per chapter (comma-separated, {total_chapters} values):")
    attempts = list(map(int, input().split(",")))

    print(f"\nEnter accuracy per chapter (%) (comma-separated, {total_chapters} values):")
    accuracies = list(map(float, input().split(",")))

    if len(attempts) != total_chapters or len(accuracies) != total_chapters:
        print("⚠️ The number of values doesn't match the total chapters.")
    else:
        # Generate chapter labels
        chapters = [f"Ch {i+1}" for i in range(total_chapters)]

        # Create DataFrame
        df = pd.DataFrame({
            "Chapter": chapters,
            "Attempts": attempts,
            "Accuracy (%)": accuracies
        })

        # Compute standard deviation
        attempts_std = stdev(attempts)
        accuracy_std = stdev(accuracies)

        # Normalize for heatmap
        df_normalized = df.copy()
        df_normalized["Attempts"] = (df["Attempts"] - df["Attempts"].min()) / (df["Attempts"].max() - df["Attempts"].min())
        df_normalized["Accuracy (%)"] = (df["Accuracy (%)"] - df["Accuracy (%)"].min()) / (df["Accuracy (%)"].max() - df["Accuracy (%)"].min())

        # --- Bar Chart ---
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        x = np.arange(len(chapters))
        width = 0.35
        ax1.bar(x - width/2, attempts, width, label='Attempts')
        ax1.bar(x + width/2, accuracies, width, label='Accuracy (%)')
        ax1.set_xticks(x)
        ax1.set_xticklabels(chapters)
        ax1.set_ylabel("Values")
        ax1.set_title("Chapter-wise Attempts and Accuracy")
        ax1.legend()
        plt.tight_layout()
        plt.show()

        # --- Heatmap ---
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.heatmap(df_normalized.set_index("Chapter").T, cmap="coolwarm", annot=True, cbar=True, ax=ax2)
        ax2.set_title("Normalized Chapter-wise Performance Heatmap")
        plt.tight_layout()
        plt.show()

        # --- Table Output ---
        print("\n=== Chapter-wise Performance Data ===")
        print(df)

        # Optional Feedback
        if attempts_std > 10 or accuracy_std > 15:
            feedback = "🚨 Inconsistent Focus Across Chapters"
        elif attempts_std > 5 or accuracy_std > 10:
            feedback = "⚠️ Mild Inconsistency – Monitor Weak Areas"
        else:
            feedback = "✅ Strong Consistency Across Syllabus"

        print(f"\n🔍 Std Dev of Attempts: {attempts_std:.2f}")
        print(f"🔍 Std Dev of Accuracy: {accuracy_std:.2f}")
        print("📝 Assessment:", feedback)

except ValueError:
    print("⚠️ Please enter valid numeric inputs.")
# This code assesses a student's chapter-wise performance based on their attempts and accuracy.