
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks: "))
    s1 = float(input("Enter subject 1 marks: "))
    s2 = float(input("Enter subject 2 marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))
    if (marks >= 75 and s1 >= 60 and s2 >= 60
            and attendance >= 75 and income <= 200000):

        students.append([name, marks, attendance, income])
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")
students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- Scholarship Ranking ---")

if len(students) == 0:
    print("No eligible students.")
else:
    for rank, student in enumerate(students, start=1):
        print("Rank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Attendance:", student[2], "%")
        print("Family Income: Rs.", student[3])
