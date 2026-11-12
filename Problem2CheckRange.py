# Islam Syndanbekov
# Date: November 4, 2026
# Problem 3: Multiply all numbers in a list

def multiplyList(numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


myList = [5, 2, 7, -1]

print("List:", myList)
print("Product:", multiplyList(myList))