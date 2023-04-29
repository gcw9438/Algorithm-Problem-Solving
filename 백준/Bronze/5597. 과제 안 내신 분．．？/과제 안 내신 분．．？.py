student = [input() for _ in range(28)]
student.sort()
for i in range(1,31):
    if str(i) not in student:
        print(i)