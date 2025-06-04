print("=== 🎓 Student Learning Style Profiler (with decimal scoring) ===")

try:
    print("\n🔹 Enter scores between 0.0 (Low) and 2.0 (High). Decimals like 1.5 are allowed.")

    # ---------------- INDIVIDUAL vs GROUP ----------------
    print("\n🔹 INDIVIDUAL vs GROUP LEARNING")

    solo_time = float(input("Time spent on solo practice: "))
    solo_perf = float(input("Performs better in solo tasks: "))
    solo_group_aversion = float(input("Low group participation: "))
    solo_pref = float(input("Prefers solo learning (survey): "))

    group_discussion = float(input("Participates in group discussions: "))
    group_projects = float(input("Completes group projects: "))
    peer_help = float(input("Helps peers with doubts: "))
    group_pref = float(input("Prefers group learning (survey): "))

    solo_score = solo_time + solo_perf + solo_group_aversion + solo_pref
    group_score = group_discussion + group_projects + peer_help + group_pref

    if solo_score - group_score >= 3:
        individual_group_assessment = "Strongly Prefers Individual Learning"
    elif solo_score - group_score >= 1:
        individual_group_assessment = "Prefers Individual Learning"
    elif group_score - solo_score >= 3:
        individual_group_assessment = "Strongly Prefers Group Learning"
    elif group_score - solo_score >= 1:
        individual_group_assessment = "Prefers Group Learning"
    else:
        individual_group_assessment = "Neutral / Adaptive Learner"

    # ---------------- VISUAL vs VERBAL ----------------
    print("\n🔹 VISUAL vs VERBAL LEARNING")

    visual_video = float(input("Time spent on videos: "))
    visual_performance = float(input("Better at visual questions: "))
    visual_pref = float(input("Prefers visuals (survey): "))

    verbal_reading = float(input("Time spent on reading: "))
    verbal_performance = float(input("Better at text questions: "))
    verbal_pref = float(input("Prefers reading/written content: "))

    visual_score = visual_video + visual_performance + visual_pref
    verbal_score = verbal_reading + verbal_performance + verbal_pref

    if visual_score - verbal_score >= 3:
        visual_verbal_assessment = "Strongly Prefers Visual Learning"
    elif visual_score - verbal_score >= 1:
        visual_verbal_assessment = "Prefers Visual Learning"
    elif verbal_score - visual_score >= 3:
        visual_verbal_assessment = "Strongly Prefers Verbal Learning"
    elif verbal_score - visual_score >= 1:
        visual_verbal_assessment = "Prefers Verbal Learning"
    else:
        visual_verbal_assessment = "Balanced Visual-Verbal Learner"

    # ---------------- VIDEO vs TEXT ----------------
    print("\n🔹 PREFERRED LEARNING MEDIUM")

    video_time = float(input("Time spent watching videos: "))
    video_complete = float(input("Completes video modules: "))
    video_survey = float(input("Prefers video content (survey): "))

    text_time = float(input("Time spent reading lessons: "))
    text_complete = float(input("Completes text modules: "))
    text_survey = float(input("Prefers text content (survey): "))

    video_score = video_time + video_complete + video_survey
    text_score = text_time + text_complete + text_survey

    if video_score - text_score >= 3:
        medium_assessment = "Strong Preference: Videos"
    elif video_score - text_score >= 1:
        medium_assessment = "Leaning Towards Videos"
    elif text_score - video_score >= 3:
        medium_assessment = "Strong Preference: Text"
    elif text_score - video_score >= 1:
        medium_assessment = "Leaning Towards Text"
    else:
        medium_assessment = "Balanced Medium Preference"

    # ---------------- OUTPUT ----------------
    print("\n=== 📋 LEARNING STYLE SUMMARY ===")
    print("1. Individual vs Group:", individual_group_assessment)
    print("2. Visual vs Verbal:", visual_verbal_assessment)
    print("3. Preferred Medium (Video/Text):", medium_assessment)

except ValueError:
    print("⚠️ Please enter decimal values between 0.0 and 2.0 only.")
# This code profiles a student's learning style based on their preferences and performance in different learning modes.
# It categorizes them into individual vs group, visual vs verbal, and preferred medium (video vs text).