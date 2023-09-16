student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"
for std in student_scores:
  score = student_scores[std]
  if score > 90:
    student_grades[std] = "Outstanding"
  elif score > 80 :
    student_grades[std] = "Exceed Expectations"
  elif score > 70 :
    student_grades[std] = "Acceptable"
  else:
    student_grades[std] = "Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇

# 🚨 Don't change the code below 👇
print(student_grades)
