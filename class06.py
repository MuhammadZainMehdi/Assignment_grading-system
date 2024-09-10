record = []
n : int = int(input("Enter no. of students: "))
for i in range(n):
    name : str = input("Enter Your Name: ")
    regID : int = int(input("Enter Your ID: "))
    phy : int = int(input("Enter Physics marks: "))
    math : int = int(input("Enter Maths marks: "))
    eng : int = int(input("Enter English marks: "))
    print()

    student_record = [name, regID, phy, math, eng]
    record.append(student_record)

for i in range(n):
    percent = (record[i][2] + record[i][3] + record[i][4]) * 100 // 300

    if percent >= 90:
        grade = "A+"

    elif percent >= 80 and percent < 90:
        grade = "A"

    elif percent >= 70 and percent < 80:
        grade = "B"

    elif percent >= 60 and percent < 70:
        grade = "C"

    elif percent >= 50 and percent < 60:
        grade = "D"

    else:
        grade = "F"

    print("\t\tGrade Report")
    print("Student Name: {} \tRoll No: {}".format(record[i][0], record[i][1]))
    print("\nSubject \tMarks Obtained")
    print("Physics \t{}/100".format(record[i][2]))
    print("Maths \t\t{}/100".format(record[i][3]))
    print("English \t{}/100".format(record[i][4]))
    print("Percentage: {}%\t\tGrade: {}".format(percent, grade))
    print()