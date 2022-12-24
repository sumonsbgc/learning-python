name = input("What is your name? ")
print("Hello "+ name)

stdRoll = int(input("What is your Roll Number? "))
print("Roll Number", stdRoll)

gradePoint = float(input("What is your grade point? "))
print("Grade Point", gradePoint)

isTeacher = input("Are you a teacher?, (Yes/No): ")

if isTeacher == "Yes":
  isTeacher = True
else:
  isTeacher = False

if isTeacher == True:
  print(name + " is a teacher.")
else:
  print(name + " is a student")