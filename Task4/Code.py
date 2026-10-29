student_id = input("Enter Student ID (YYBBBSSSS): ").upper()
branches = ["CSE", "ECE", "EEE"]
if (len(student_id) == 9
    and student_id[:2].isdigit()
    and student_id[2:5] in branches
    and student_id[5:].isdigit()):
    year = "20" + student_id[:2]
    branch = student_id[2:5]
    number = student_id[5:]
    print("\n--- STUDENT DETAILS ---")
    print("Admission Year:", year)
    print("Branch:", branch)
    print("Student Number:", number)
    print("Classification:", branch, year, "Batch")
else:
    print("Invalid Student ID!")

