mySet  = {'peach', 'apple', 'banana', 'cherry'}
myList = ['banana', 'kiwi']
for item in myList:
    if item in mySet:
        mySet.remove(item)
    print(mySet)