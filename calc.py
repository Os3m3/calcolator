firstNumber = float(input("Enter the First Number: "))
operator = input("Enter the Operator: ")
secondNumber = float(input("Enter the Second Number: "))


if operator == "+":
    print("The Answer is:", firstNumber + secondNumber)

elif operator == "-":
    print("The Answer is:", firstNumber - secondNumber)

elif operator == "*":
    print("The Answer is:", firstNumber * secondNumber)

elif operator == "/":
    print("The Answer is:", firstNumber / secondNumber)

elif operator == "^":
    print("The Answer is:", pow(firstNumber, secondNumber))

elif operator == "abs":
    print("The Answer is:", abs(firstNumber + secondNumber))

elif operator == "%":
    print("The Answer is:", firstNumber % secondNumber)

else:
    print("Please Try Again Sad :(")