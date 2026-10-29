
n = int(input("Enter number of students: "))for i in range(n): 
print("\nStudent", i + 1) 
name = input("Enter student name: ")  
marks = float(input("Enter aggregate marks: "))  
s1 = float(input("Enter subject 1 marks: "))  
s2 = float(input("Enter subject 2 marks: ")) 
attendance = float(input("Enter attendance percentage: ")) 
income = float(input("Enter annual family income: "))  
if (marks >= 75 and s1 >= 60 and s2 >= 60  
 attendance >= 75 and income <= 200000):    
 students.append([name, marks, attendance, income])   
 print("Eligible for scholarship")  
 else:        print("Not eligible for scholarship")

- Aggregate marks must be at least 75%.
- Each subject must have at least 60 marks.
- Attendance must be at least 75%.
- Annual family income must not exceed ₹2,00,000

1. Higher aggregate marks get a higher rank.
2. If marks are equal, higher attendance gets a higher rank.
3. If both are equal, lower family income gets a higher range

1. Enter each student's details.
2. Check all eligibility conditions.
3. Store eligible students in a list.
4. Sort students using the tie-breaking rules.
5. Display the final scholarship ranking.
