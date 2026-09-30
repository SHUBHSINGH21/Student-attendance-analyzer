#this file is related to reports
from data import students, subjects
from attendance import calculate_percentage
def subject_report():
    print("\n----- SUBJECT REPORT -----")
    for subject in subjects:
        total_percentage = 0
        count = 0
        low_students = []
        print("\nSubject:", subject)
        for roll, student in students.items():
            present = student["attendance"][subject][0]
            total = student["attendance"][subject][1]
            percentage = calculate_percentage(present, total)
            total_percentage += percentage
            count += 1

            if percentage < 75:
                low_students.append(student["name"])

        if count > 0:
            average = total_percentage / count
        else:
            average = 0
        print("Class Average:", round(average, 2), "%")

        if low_students:
            print("Students below 75%:")

            for name in low_students:
                print("-", name)

        else:
            print("No student is below 75%.")

# low attendance
def low_attendance():
    print("\n----- LOW ATTENDANCE STUDENTS -----")
    found = False
    for roll, student in students.items():
        total_present = 0
        total_classes = 0
        for subject in subjects:

            present = student["attendance"][subject][0]
            total = student["attendance"][subject][1]

            total_present += present
            total_classes += total

        percentage = calculate_percentage(
            total_present,
            total_classes)
        

        if percentage < 75:

            found = True

            print(
                roll,
                "-",
                student["name"],
                "-",
                round(percentage, 2),
                "%")
            

    if not found:
        print("No student has attendance below 75%.")

# class summary
def class_summary():

    print("\n========== CLASS SUMMARY ==========")

    print("Total Students:", len(students))
    print("Total Subjects:", len(subjects))

    for subject in subjects:

        total_present = 0
        total_classes = 0

        for student in students.values():

            total_present += student["attendance"][subject][0]
            total_classes += student["attendance"][subject][1]

        percentage = calculate_percentage(
            total_present,
            total_classes)

        print(
            subject,
            ":",
            round(percentage, 2),
            "%")
