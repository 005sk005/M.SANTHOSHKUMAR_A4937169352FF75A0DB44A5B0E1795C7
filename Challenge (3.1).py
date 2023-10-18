# Python3 program to calculate the CGPA
# and CGPA percentage of a student
def CgpaCalc(marks, n):

  # Variable to store the grades in
  # every subject
  grade = [0] * n

  # Variables to store CGPA and the
  # sum of all the grades
  Sum = 0

  # Computing the grades
  for i in range(n):
    grade[i] = (marks[i] / 10)

  # Computing the sum of grades
  for i in range(n):
    Sum += grade[i]

  # Computing the CGPA
  cgpa = Sum / n

  return cgpa


# Driver code
n = 5
marks = [100, 100,100, 100, 100]

cgpa = CgpaCalc(marks, n)

print("CGPA = ", '%.1f' % cgpa)
print("CGPA Percentage = ", '%.2f' % (cgpa * 10))
#This Code created by M SANTHOSH Kumar 