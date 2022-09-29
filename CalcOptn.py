#Displaying operations
print("OPERATIONS")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")

#Choose an operation to perform
operation = int(input("Select an operation to perform: "))

#Perform calculations and display results
if operation == 1:
    frstNum = int(input("Enter the first number: "))
    scndNum = int(input("Enter the second number: "))
    addNums = frstNum + scndNum
    print("The result is:", addNums)
elif operation == 2:
    frstNum = int(input("Enter the first number: "))
    scndNum = int(input("Enter the second number: "))
    subNums = frstNum - scndNum
    print("The result is:",subNums)
elif operation == 3:
    frstNum = int(input("Enter the first number: "))
    scndNum = int(input("Enter the second number: "))
    multNums = frstNum * scndNum
    print("The result is:",multNums)
elif operation == 4:
    frstNum = int(input("Enter the first number: "))
    scndNum = int(input("Enter the second number: "))
    divNums = frstNum / scndNum
    print("The result is:",divNums)
else:
    print("Invalid Entry!! Try Again.")