n = int(input("how many numbers u want nga:"))
numbers = []
for x in range(n):
    num = int(input("Insert a Number"))
    numbers.append(num)
print(numbers)
numbers.sort()
print(numbers)