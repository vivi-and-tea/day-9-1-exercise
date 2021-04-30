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

#TODO-2: Write your code below to add the grades to student_grades.👇
for stn in student_scores:

  if student_scores[stn] >= 91:
    student_grades[str(stn)] = "Outstanding"
  if student_scores[stn] >= 81 and student_scores[stn] <= 90:
    student_grades[str(stn)] = "EXCEEDS"
  if student_scores[stn] >= 71 and student_scores[stn] <= 80:
    student_grades[str(stn)] = "ACCEPTABLE"
  if student_scores[stn] <= 70:
    student_grades[str(stn)]  = "FAIL"

# 🚨 Don't change the code below 👇
print(student_grades)





