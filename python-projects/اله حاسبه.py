num1 =(input( "Enter the first number: "))
num2 =(input("enter the second number: "))

operation = input("Select the operation(+ - * /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("the option is not right")
    exit()

print("result:", result)

if num1 > num2:
    print("the first number is bigger than a second number")
elif num1 < num2:
    print("the first number is the smaller than second number")
else:
    print("both numbers are equal")
