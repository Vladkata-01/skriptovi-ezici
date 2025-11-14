list = ['apple', 'orange', 'watermelon', 'banana', 'apple']

duplicates = False

for i in range(Len(list)):
    for x in range(i + 1 , Len(list)):
        if list[i] == list[x]:
            duplicates = True
            print("Duplicate found:", list[i])