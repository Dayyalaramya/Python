name = input("Enter student name: ")

m1 = float(input("Enter marks in English: "))
m2 = float(input("Enter marks in Python: "))
m3 = float(input("Enter marks in Maths: "))

total = m1 + m2 + m3
average = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)