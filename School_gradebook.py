class Student:
    def __init__(self, name, gender, points):
        self.name = name
        self.gender = gender
        self.points = int(points)
        self.grade = 2 + self.points / 25


n = int(input("N = "))

students = []

for i in range(n):
    name, gender, points = input().split()
    students.append(Student(name, gender, points))


total = 0
m_total = 0
w_total = 0
m_count = 0
w_count = 0

for s in students:
    total += s.grade

    if s.gender == "M":
        m_total += s.grade
        m_count += 1
    else:
        w_total += s.grade
        w_count += 1


avg = total / n
m_avg = m_total / m_count
w_avg = w_total / w_count

print(f"Average: {avg:.2f}")
print(f"M Average: {m_avg:.2f}")
print(f"W Average: {w_avg:.2f}")