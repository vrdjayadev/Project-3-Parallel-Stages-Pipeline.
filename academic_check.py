# academic_check.py
import time

def audit_academic_performance():
    print("[TASK B] Starting Parallel Academic Records Formula Audit...")
    time.sleep(3)  # Simulates processing latency

    # Sample gradebook evaluations
    gradebook = [
        {"student_id": "STU1001", "assignment_score": 85, "exam_score": 90},
        {"student_id": "STU1002", "assignment_score": 92, "exam_score": 45},
        {"student_id": "STU1003", "assignment_score": -10, "exam_score": 88}, # Invalid Negative Score
        {"student_id": "STU1004", "assignment_score": 78, "exam_score": 105} # Invalid Score > 100
    ]

    discrepancies = 0

    print("\n--- Auditing Academic Gradebooks ---")
    for record in gradebook:
        errors = []
        sid = record["student_id"]
        
        # Rule 1: Validate score boundaries (0 to 100)
        for assessment, score in [("Assignment", record["assignment_score"]), ("Exam", record["exam_score"])]:
            if score < 0 or score > 100:
                errors.append(f"Out-of-bounds {assessment} score encountered: {score}")

        if errors:
            discrepancies += 1
            print(f"❌ Academic Registry Bug in {sid}:")
            for err in errors:
                print(f"   - {err}")
        else:
            # Logic: Weighted GPA evaluation (40% Assignments + 60% Exam)
            final_grade = (record["assignment_score"] * 0.4) + (record["exam_score"] * 0.6)
            print(f"✅ Grades Valid for {sid} | Aggregated Weighted Final Grade: {final_grade:.2f}%")

    print("\n--- Academic Evaluation Summary ---")
    if discrepancies > 0:
        print(f"Status: Complete. Flagged {discrepancies} structural math calculation failures.")
    else:
        print("Status: Success. Data equations verified across all matching indices.")

if __name__ == "__main__":
    audit_academic_performance()
