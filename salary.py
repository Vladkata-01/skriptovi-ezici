N = int(input("Enter number of employees(between 1 and 1000):"))
salary = int(input("enter salary:"))
p1 = p2 =p3 = p4 =p5 = 0
for i in range(N):
    if salary < 200:
        p1 += 1
    elif 200 <= salary < 400:
        p2 += 1
    elif 400 <= salary < 600:
        p3 += 1
    elif 600 <= salary < 800:
        p4 += 1
    elif salary > 800:
        p5 += 1
    print (f"from 0 to 199: {p1 / N * 100: .2f}%")
    print (f"from 200 to 399: {p2 / N * 100: .2f}%")
    print (f"from 400 to 599: {p3 / N * 100: .2f}%")
    print (f"from 600 to 799: {p4 / N * 100: .2f}%")
    print (f"from 800 and more: {p5 / N * 100: .2f}%")