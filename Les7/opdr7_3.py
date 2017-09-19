student_grades = {
    "Bob": 6.0,
    "Sjon": 3.0,
    "Hans": 10.0,
    "Sjors": 9.3,
    "Robbert": 7.0,
    "Kim": 4.8,
    "Timo": 6.4,
    "Kees": 9.0
}

for student in student_grades:
    if student_grades[student] >= 9.0:
        print("{0} heeft een {1} behaald!".format(student, student_grades[student]))
