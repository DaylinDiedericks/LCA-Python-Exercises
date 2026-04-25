import math_operations
#QUestion1:
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(fruit)

#Question2:
count = 5 
while count >= 1:
    print(count)
    count -= 1

#Question3:
for i in range(1, 11):
    print(i * i)

#Question4:
import random
colors = ["red", "blue", "green", "yellow", "purple"]
for  i in range(3):
    print(random.choices(colors))

 #Question5:
import math_operations
#Example usage
print(math_operations.add(10, 5))
print(math_operations.subtract(10, 5))
print(math_operations.multiply(10, 5))
print(math_operations.divide(10, 5))

#Simple calculator
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /) or 'q' to quit: ")
    if op == 'q':
        print("Calculator closed.")
        break
    if op == '+':
        print("Result:", math_operations.add(num1, num2))
    elif op == '-':
        print("Result:", math_operations.subtract(num1, num2))
    elif op == '*':
        print("Result:", math_operations.multiply(num1, num2))
    elif op == '/':
        print("Result:", math_operations.divide(num1, num2))
    else:
        print("Invalid operation")
