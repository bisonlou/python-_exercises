def grade_marks():
    marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]
    marks_less_than_50 = []
    marks_greater_than_50 = []

    for mark in marks:
        mark_sets = []
        if mark  > 50:
            marks_greater_than_50.append(mark)
        else:
            marks_less_than_50.append(mark)

    mark_sets.append(marks_greater_than_50)
    mark_sets.append(marks_less_than_50)
    
    for mark in marks:
        if mark >=90:
            print("{} : Excellent".format(mark))
        elif mark >= 70 and mark <= 89:
            print( "{} : Very Good".format(mark))
        elif mark >= 60 and mark <=69:
            print( "{} : Good".format(mark))
        elif  mark >= 40 and mark <=59:
            print( "{} : Poor".format(mark))
        elif mark >= 20 and mark <= 39:
            print( "{} : Very Poor".format(mark))
        elif  mark <= 19:
            print( "{} : repeat".format(mark))

print(grade_marks())
    


