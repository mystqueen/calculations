#Addition
def addition(num1, num2):
    return num1 + num2
    
#Subtraction
def subtraction(num1, num2):
    return num1 - num2
    
#Multiplication
def multiplication(num1, num2):
    return num1 * num2
    
#Division
def division(num1, num2):
    return num1 / num2

userInput = input("1.Add \n2.Subtract \n3.Multiply \n4.Divide \nSelect an operation: ")
firstNum = float(input("Enter the first number: "))
secondNum = float(input("Enter second number: "))

if userInput == "1":
    print(addition(firstNum, secondNum))
elif userInput == "2":
    print(subtraction(firstNum, secondNum))
elif userInput == "3":
    print(multiplication(firstNum, secondNum))
elif userInput == "4":
    print(division(firstNum, secondNum))
else :
    print("Invalid Input!!!")
    