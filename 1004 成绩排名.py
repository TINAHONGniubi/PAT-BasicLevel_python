1004 成绩排名：读入 n（>0）名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。

n = int(input()) #输入学生人数
#print(n)

#列表存储学生信息
students = []

#读取, input().split() 读取每个学生的姓名、学号和成绩。
for _ in range(n):
    name, student_id, score = input().split()
    score = int(score)
    students.append((name, student_id, score))
    #print(students)

#排序
students_sorted = sorted(students, key=lambda student: student[2])

#最高分和最低分
lowest_student = students_sorted[0]
highest_student = students_sorted[-1]

print(f"{highest_student[0]} {highest_student[1]}")
print(f"{lowest_student[0]} {lowest_student[1]}")
