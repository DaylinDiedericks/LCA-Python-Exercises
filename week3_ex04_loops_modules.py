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
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#Example usage
print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

#Simple calculator
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /) or 'q' to quit: ")
    if op == 'q':
        print("Calculator closed.")
        break
    if op == '+':
        print("Result:", add(num1, num2))
    elif op == '-':
        print("Result:", subtract(num1, num2))
    elif op == '*':
        print("Result:", multiply(num1, num2))
    elif op == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")
