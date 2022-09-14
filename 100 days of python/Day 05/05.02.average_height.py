# 🚨 Don't change the code below 👇
from itertools import count


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
total_height = 0
for i in student_heights:
    total_height += i
    count += 1
print(round(total_height/count,2))

