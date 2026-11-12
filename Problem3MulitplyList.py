# Islam Syndanbekov
# Date: November 4, 2026
# Problem 4: Return unique elements from a list

def uniqueElements(numbers):
    uniqueList = []

    for number in numbers:
        if number not in uniqueList:
            uniqueList.append(number)

    return uniqueList


myList = [1, 3, 3, 3, 6, 2, 3, 5]

print("Original list:", myList)
print("Unique elements:", uniqueElements(myList))