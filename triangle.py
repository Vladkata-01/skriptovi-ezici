def area(a , b):
    c = (a * a + b * b) ** 0.5
    S = 0.5 * (a * b)
    P = a + b + c
    return S,P
a = float(input("a:"))
b = float(input("b:"))
S,P = area(a, b)
print (f"Area: {S}")
print(f"Perimeter: {P}")
    