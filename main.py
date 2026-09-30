

print("===== Student Information =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n Enter your marks: ")

english = int(input("English Marks: "))
maths = int(input("Maths Marks: "))
computer = int(input("Computer Marks: "))

total = english + maths + computer
percentage = total / 300 * 100

print("\n ===== Result =====")
print("Name: ", name)
print("Age: ", age)
print("Total Marks: ", total)
print("Percentage: ", percentage, "%")

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade: ", grade)