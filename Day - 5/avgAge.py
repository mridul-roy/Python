
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height


num_of_student = 0
for student in student_heights:
  num_of_student += 1


print(round(total_height/num_of_student))