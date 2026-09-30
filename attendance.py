#This file for attendance
from data import students, subjects
def add_student():
    roll = int(input("Enter roll number: "))
    if roll in students:
        print("Student already exists.")
        return
    name = input("Enter student name: ")
    students[roll] = {
        "name": name,
        "attendance": {}
    }
    for subject in subjects:
        students[roll]["attendance"][subject] = [0, 0]
        print("Student added successfully.")
# subject
def add_subject():
    subject = input("Enter subject name: ")
    if subject in subjects:
        print("Subject already exists.")
        return
    subjects.append(subject)
    for student in students.values():
        student["attendance"][subject] = [0, 0]
        print("Subject added successfully.")
# attendance mark
def mark_attendance():
    if not students:
        print("No students available.")
        return
    print("\nStudents:")
    for roll, student in students.items():
        print(roll, "-", student["name"])
    roll = int(input("Enter roll number: "))
    if roll not in students:
        print("Student not found.")
        return
    print("\nSubjects:")
    for i in range(len(subjects)):
        print(i + 1, ".", subjects[i])
        choice = int(input("Select subject: "))
        if choice < 1 or choice > len(subjects):
            print("Invalid subject.")
            return
        subject = subjects[choice - 1]
        print("1. Present")
        print("2. Absent")

    status = int(input("Enter attendance: "))
    if status == 1:
        students[roll]["attendance"][subject][0] += 1
        students[roll]["attendance"][subject][1] += 1
        print("Marked Present.")

    elif status == 2:
        students[roll]["attendance"][subject][1] += 1
        print("Marked Absent.")

    else:
        print("Invalid choice.")

# percentage calculation
def calculate_percentage(present, total):
    if total == 0:
        return 0

    return (present / total) * 100


def student_attendance():
    roll = int(input("Enter roll number: "))

    if roll not in students:
        print("Student not found.")
        return

    student = students[roll]

    print("\n--------------------------------")
    print("Student:", student["name"])
    print("Roll Number:", roll)
    print("--------------------------------")

    for subject in subjects:

        present = student["attendance"][subject][0]
        total = student["attendance"][subject][1]

        percentage = calculate_percentage(present, total)

        print(
            subject,
            ":", present, "/", total,
            "=", round(percentage, 2), "%"
        )


def show_all_students():
    print("\n----- ALL STUDENTS -----")

    for roll, student in students.items():
        print(roll, "-", student["name"])
