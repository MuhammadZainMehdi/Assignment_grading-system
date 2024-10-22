name : str = input("Enter Your Name: ")
regID : int = int(input("Enter Your ID: "))
oop : int = int(input("Enter OOP marks: "))
db : int = int(input("Enter Database marks: "))
ds : int = int(input("Enter Discrete marks: "))

percent = (oop + db + ds) * 100 // 300

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

elif percent >= 40 and percent < 50:
    grade = "E"

else:
    grade = "F"


print("\t\tGrade Report")
print("\nStudent Name: {} \tRoll No: {}".format(name, regID))
print("\nSubject\t Marks Obtained\t Total Marks")
print("Object Oriented\t {} \t 100".format(oop))
print("Database\t {} \t 100".format(db))
print("Discrete\t {} \t 100".format(ds))

print("\nTotal Marks: {}".format(oop+db+ds))
print("Percentage: {}%".format(percent))
print("Grade: {}".format(grade))