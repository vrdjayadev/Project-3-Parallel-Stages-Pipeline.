# student_check.py
import time

def validate_student_data():
    print("[TASK A] Starting Parallel Student Profile Validation...")
    time.sleep(3)  # Simulates processing latency

    # Sample student data database records
    student_records = [
        {"student_id": "STU1001", "name": "V R D Jayadevan", "age": 20},
        {"student_id": "STU1002", "name": "Rajkamal V R D", "age": 22},
        {"student_id": "STU1003", "name": "Anand Vijay", "age": 21},
        {"student_id": "STU1004", "name": "", "age": 19},           # Invalid Name
        {"student_id": "STU100",  "name": "Dhanesh Babu", "age": 23} # Invalid ID Length
    ]

    failures = 0

    print("\n--- Auditing Student Profiles ---")
    for idx, student in enumerate(student_records, 1):
        errors = []
        
        # Rule 1: ID format validation (Must start with STU and be 7 characters long)
        if not student["student_id"].startswith("STU") or len(student["student_id"]) != 7:
            errors.append(f"Invalid format or length for ID '{student['student_id']}'")
            
        # Rule 2: Non-empty name validation
        if not student["name"].strip():
            errors.append("Student record contains an empty name field")
            
        # Rule 3: Age safety boundary checks
        if not (17 <= student["age"] <= 30):
            errors.append(f"Age {student['age']} falls outside expected university parameters (17-30)")

        if errors:
            failures += 1
            print(f"❌ Record {idx} Failed Validation:")
            for err in errors:
                print(f"   - {err}")
        else:
            print(f"✅ Record {idx} ({student['student_id']} - {student['name']}): Profile Valid.")

    print("\n--- Student Validation Summary ---")
    if failures > 0:
        print(f"Status: Complete. Detected {failures} non-compliant profiles. Flagging warning actions.")
    else:
        print("Status: Success. All records comply with data system parameters.")

if __name__ == "__main__":
    validate_student_data()
