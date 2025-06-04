print("=== Student Learning Velocity Assessment ===")

try:
    # Inputs
    previous_score = float(input("Enter previous test score: "))
    current_score = float(input("Enter current test score: "))
    days_between_tests = int(input("Enter number of days between tests: "))

    # Basic checks
    if previous_score == 0 or days_between_tests <= 0:
        improvement_ratio = 0.0
        velocity = 0.0
        assessment = "Insufficient Data"
    else:
        # Calculations
        improvement = current_score - previous_score
        improvement_ratio = improvement / previous_score
        velocity = improvement / days_between_tests

        # Assessment logic
        if improvement_ratio >= 0.3 and velocity >= 0.5:
            assessment = "Rapid Improver"
        elif improvement_ratio >= 0.15 and velocity >= 0.2:
            assessment = "Consistent Improver"
        elif improvement_ratio > 0:
            assessment = "Slow Improvement"
        elif improvement_ratio == 0:
            assessment = "No Change"
        else:
            assessment = "Performance Dropped"

    # Output
    print("\n=== Result ===")
    print("Improvement Ratio:", round(improvement_ratio * 100, 2), "%")
    print("Learning Velocity:", round(velocity, 2), "points/day")
    print("Assessment:", assessment)

except ValueError:
    print("⚠️ Please enter valid numerical values.")
# This code assesses a student's learning velocity based on their test scores and the time between tests.