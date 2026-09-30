

def student_grading(name,score):

    if score >=70 and score <= 100:
        grade = "A"

    elif score >=60 and score <= 69:
        grade = "B"

    elif score >=50 and score <= 59:
        grade = "C"

    elif score >=45 and score <= 49:
       grade = "D"

    elif score >=40 and score <= 44:
        grade = "E"

    else:
        grade = "F"
    return f"{name}, {score}, {grade}"



#     return f"{names},{scores}"