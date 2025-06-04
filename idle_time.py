print("=== 🧠 Attention Span & Idle Time Assessment ===")

try:
    # Inputs
    idle_time = float(input("Average idle time per session (in seconds): "))
    tab_switching = float(input("Rate tab-switching/app exits (0=never, 2=frequent): "))
    drop_off = float(input("Drop-off rate before module completion (0–2): "))

    # Normalize idle time (you can tweak thresholds)
    if idle_time < 30:
        idle_score = 2.0  # good attention
    elif idle_time <= 90:
        idle_score = 1.0
    else:
        idle_score = 0.0  # high idle time = poor attention

    # Final score out of 6
    total_attention_score = idle_score + (2 - tab_switching) + (2 - drop_off)

    # Assessment
    if total_attention_score >= 5:
        label = "🧠 Highly Attentive"
    elif total_attention_score >= 3:
        label = "⚠️ Moderately Focused"
    else:
        label = "🚨 Low Attention / Easily Distracted"

    # Output
    print("\n=== 📋 ATTENTION REPORT ===")
    print(f"Idle Score: {idle_score} / 2.0")
    print(f"Tab Switching Penalty: {tab_switching}")
    print(f"Drop-off Penalty: {drop_off}")
    print(f"Total Focus Score: {total_attention_score:.2f} / 6.0")
    print("Assessment:", label)

except ValueError:
    print("⚠️ Please enter valid decimal or numeric values.")
# This code assesses a student's attention span and idle time based on their input data.