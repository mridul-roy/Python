student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

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

print(student_grades)
