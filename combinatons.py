def combinations(numbers, k):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)): 
            if numbers[i] + numbers[j] > k:
                print(f"({numbers[i]}, {numbers[j]})")


numbers = [1, 5, 2, 8, 3]
k = 7
combinations(numbers, k)