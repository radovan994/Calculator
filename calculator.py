
def addition():
    print('You have selected addition.')
    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter a number to add: '))
    return num1 + num2
    
def subtraction():
    print('You have selected subtraction.')
    num1 = float(input('Enter the minuend: '))
    num2 = float(input('Enter the subtrahend: '))
    return num1 - num2

def multiplication():
    print('You have selected multiplication.')
    num1 = float(input('Enter a number: '))
    num2 = float(input("Enter it's multiplier: "))
    return num2*num1

def division():
    print('You have selected division.')
    num1 = float(input('Please enter the dividend: '))
    num2 = float(input('Please enter the divisor: '))
    if num2 != 0:
        return num1/num2
    else:
        print('Cannot divide by zero')

while True:
    result = 0
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'd' for division")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            result = addition()
            print("Ans = " + str(result))
        elif c == 's':
            result = subtraction()
            print("Ans = " + str(result))
        elif c == 'm':
            result = multiplication()
            print("Ans = " + str(result))
        elif c == 'd':
            result = division()
            print("Ans = " + str(result))
        else:
            print ("Sorry, invilid character")
    else:
        break
