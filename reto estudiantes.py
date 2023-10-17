https://replit.com/join/ronriffnte-lucasleite32

grades = []

students = int(input("How many students there are in the class? "))
print()

for i in range(students):
  presence = input("Is the student " + str(i + 1) + " present? ")
  print()
  grade = int(input("Grade Student " + str(i + 1) + ": "))
  
  grades.append(grade)
  average = sum(grades) / len(grades)
  print()
  print("The average grade is: " + str(average))
  print()
  
  if average >= 75 and average < 90 and presence == "yes":
      print("The student are in a good academic standing")
      
  elif average > 90 and presence == "yes":
      print("The student receive a distinction")
      
  elif average < 60 and presence == "no":
      print("The student needs to improve their performance")
