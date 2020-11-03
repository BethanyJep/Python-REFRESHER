# Create a FUNCTION to find if provided year is leap or not .(Yearshouldbeparsed as aparameter).

year = int(input('Enter a year: '))

def leapYear(year):
    if (year % 4) == 0:
        print('this is a leap year')
    else:
        print('this is not a leap year')

leapYear(year)

# Given three number/variables A, B and C;
# The task is to create a FUNCTION to find the largest number among the three.
# (the variables should be parsed as parameters).

A = int(input('Enter number A: '))
B = int(input('Enter number B: '))
C = int(input('Enter number C: '))

def largestNumber():
    numberList = []
    numberList.append(A)
    numberList.append(B)
    numberList.append(C)
    numberList.sort()
    print('Largest number is: ', numberList[2])

largestNumber()