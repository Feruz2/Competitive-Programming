def gradingStudents(grades):
    # Write your code here
    li =[]
    for grade in grades:
        if grade <35:
            li.append(grade)
            continue
        rem = 5 - grade%5
        rounded = rem + grade
        if rem >= 3:
            li.append(grade)
            continue
        grade = rounded
        li.append(grade)
    return li
