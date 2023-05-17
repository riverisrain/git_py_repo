student = []


for i in range(1,31):
    student.append(i)



for j in range(1,29):
    applied = int(input())
    student.remove(applied)

print(min(student))
print(max(student))
