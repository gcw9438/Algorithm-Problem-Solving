grades = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0}
grade = input()
if grade == 'F':
    print(0.0)
elif grade[1] == '+':
    print(grades[grade[0]] + 0.3)
elif grade[1] == '0':
    print(grades[grade[0]])
elif grade[1] == '-':
    print(grades[grade[0]] - 0.3)