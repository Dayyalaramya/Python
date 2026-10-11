name = input("Enter student name: ")

marks1 = int(input("Enter marks in Python: "))
marks2 = int(input("Enter marks in SQL: "))
marks3 = int(input("Enter marks in Excel: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")