kilometers = int(input("Amount of kilometers travelled:"))
time = input("Day or night:")
sum = 0

if kilometers > 100:
    sum = 0.06 *kilometers
elif kilometers > 20:
    sum = 0.09 *kilometers
else:
    if time == "day":
        sum = 0.70 + 0.79 *kilometers
    elif time == "night":
        sum = 0.70 + 0.90 *kilometers

print(f"sum = {sum}")

