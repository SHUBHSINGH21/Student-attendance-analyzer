from attendance import (
    add_student,
    add_subject,
    mark_attendance,
    student_attendance,
    show_all_students
)
from reports import (
    subject_report,
    low_attendance,
    class_summary
)
def menu():
    while True:
        print("\n")
        print("======================================")
        print("       CLASS ATTENDANCE ANALYZER")
        print("======================================")
        print("1. Add Student")
        print("2. Add Subject")
        print("3. Mark Attendance")
        print("4. View Student Attendance")
        print("5. View All Students")
        print("6. Subject Report")
        print("7. Low Attendance Students")
        print("8. Class Summary")
        print("9. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_student()

        elif choice == "2":
            add_subject()

        elif choice == "3":
            mark_attendance()

        elif choice == "4":
            student_attendance()

        elif choice == "5":
            show_all_students()

        elif choice == "6":
            subject_report()

        elif choice == "7":
            low_attendance()

        elif choice == "8":
            class_summary()

        elif choice == "9":
            print("Thank you for using Class Attendance Analyzer.")
            break

        else:
            print("Invalid choice. Please try again.")
menu()