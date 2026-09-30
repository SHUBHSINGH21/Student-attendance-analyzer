#  Class Attendance Analyzer

A simple **Python-based Class Attendance Analyzer** that helps manage student attendance, calculate attendance percentages, and generate useful class reports.

This project is built as a **console-based application** and is designed to keep attendance management simple and easy to understand.

---

##  Features

The application provides the following options:

1. **Add Student** – Add a new student using their roll number and name.
2. **Add Subject** – Add a new subject to the class.
3. **Mark Attendance** – Mark a student as Present or Absent for a subject.
4. **View Student Attendance** – Check a student's attendance subject-wise.
5. **View All Students** – Display all registered students.
6. **Subject Report** – View the average attendance for each subject.
7. **Low Attendance Students** – Find students whose attendance is below 75%.
8. **Class Summary** – View an overall summary of students, subjects, and subject attendance.
9. **Exit** – Close the application.

The main menu connects these different features together.

---

##  Technologies Used

* **Python 3**
* Python Dictionaries
* Python Lists
* Functions
* Modules and Imports
* Console-based User Interface

No external Python libraries are required.

---

##  Project Structure

```text
Class-Attendance-Analyzer/
│
├── main.py
├── attendance.py
├── data.py
├── reports.py
└── README.md
```

### `main.py`

This is the main entry point of the project.

It displays the application menu and calls the required functions from `attendance.py` and `reports.py`.

### `attendance.py`

This module handles attendance-related operations, including:

* Adding students
* Adding subjects
* Marking attendance
* Calculating attendance percentage
* Viewing individual student attendance
* Displaying all students

### `data.py`

This file stores the student and subject data used by the application.

The sample project currently contains three students and three subjects:

* Python
* Calculus
* English

### `reports.py`

This module is responsible for generating reports such as:

* Subject-wise attendance reports
* Students with attendance below 75%
* Class summary

---

##  How Attendance Is Stored

Attendance for each subject is stored in the following format:

```python
[Present, Total]
```

For example:

```python
"Python": [18, 20]
```

This means the student was present for **18 out of 20 classes**.

The attendance percentage is calculated using:

```text
(Present / Total) × 100
```

If no classes have been conducted, the percentage is returned as `0`.

---

##  Attendance Threshold

The project uses **75%** as the attendance threshold.

Students whose attendance percentage is below 75% are included in the low-attendance reports.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Class-Attendance-Analyzer.git
```

### 2. Open the project folder

```bash
cd Class-Attendance-Analyzer
```

### 3. Run the application

```bash
python main.py
```

> Make sure Python 3 is installed on your system.

---

## 🖥️ Example Menu

When the program starts, you will see a menu similar to:

```text
======================================
       CLASS ATTENDANCE ANALYZER
======================================

1. Add Student
2. Add Subject
3. Mark Attendance
4. View Student Attendance
5. View All Students
6. Subject Report
7. Low Attendance Students
8. Class Summary
9. Exit

Enter your choice:
```

---

##  Example Data

The project currently includes sample attendance data for:

| Student      | Python | Calculus | English |
| ------------ | -----: | -------: | ------: |
| Rahul Sharma |  18/20 |    16/20 |   19/20 |
| Aman Verma   |  14/20 |    17/20 |   15/20 |
| Riya Singh   |  20/20 |    18/20 |   19/20 |

This sample data is stored in `data.py`.

---

##  Reports

### Subject Report

The subject report calculates the average attendance for each subject and identifies students whose attendance is below 75%.

```text
----- SUBJECT REPORT -----

Subject: Python
Class Average: XX.XX %
```

### Low Attendance Report

The application also checks combined attendance across subjects and displays students below the 75% threshold.

### Class Summary

The class summary displays:

* Total number of students
* Total number of subjects
* Attendance percentage for each subject

---

##  How the Project Works

```text
                 ┌──────────────┐
                 │   main.py    │
                 │  Main Menu   │
                 └──────┬───────┘
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼
 ┌─────────────────┐         ┌─────────────────┐
 │  attendance.py  │         │   reports.py    │
 │                 │         │                 │
 │ Add Student     │         │ Subject Report  │
 │ Add Subject     │         │ Low Attendance  │
 │ Mark Attendance │         │ Class Summary   │
 │ View Attendance │         │                 │
 └────────┬────────┘         └────────┬────────┘
          │                           │
          └─────────────┬─────────────┘
                        ▼
                 ┌──────────────┐
                 │    data.py   │
                 │              │
                 │ Students     │
                 │ Subjects     │
                 │ Attendance   │
                 └──────────────┘
```

---

##  Purpose of the Project

This project was created as a practical Python project to demonstrate how basic programming concepts can be combined to build a useful application.

It demonstrates:

* Functions
* Conditional statements
* Loops
* Lists
* Dictionaries
* Modules
* User input
* Basic calculations
* Report generation

---

##  Future Improvements

Some possible improvements for future versions could include:

* Saving attendance permanently to a file or database
* Adding a graphical user interface
* Adding login/authentication
* Exporting attendance reports
* Adding dates to attendance records
* Adding more detailed student statistics
* Improving input validation

These are potential extensions rather than features currently implemented in the supplied code.

---

##  Author

**Your Name**

If you're using this project for a college or academic submission, you can replace this section with your name, course, college, and academic year.

---

##  License

This project is created for educational and learning purposes.
