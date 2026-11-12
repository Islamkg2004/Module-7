# Islam Syndanbekov
# Date: November 4, 2026
# Problem 2: Check if a number is in a given range

def checkRange(number):
    if number in range(1, 10):
        print(number, "is in the range.")
    else:
        print(number, "is not in the range.")


number = int(input("Enter a number: "))

checkRange(number)