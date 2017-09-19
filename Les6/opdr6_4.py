def average_per_student(total_grades):
    average = []
    for student_grades in total_grades:
        average.append(sum(student_grades) / len(student_grades))
    return average


def average_all_students(total_grades):
    average_grades = average_per_student(total_grades)
    return sum(average_grades) / len(average_grades)


grades = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

print("Gemiddelde per student: {0}".format(average_per_student(grades)))
print("Gemiddelde van alle studenten: {0}".format(average_all_students(grades)))