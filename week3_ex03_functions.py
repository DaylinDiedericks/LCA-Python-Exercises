#Question1:
def greet():
    print("Hello, World!")
#Call function
greet()

#Question2:
def personalized_greeting(name):
    print("Hello, ", name + "!")
#Call function
personalized_greeting("Daylin")

#Question3:
def sqaure(number):
    return number * number
#Call function
result = sqaure(5)
print("Square of 5 is:",result)

#Question4:
def rectangle_area(length, width):
    return length * width
#Call function
area = rectangle_area(4, 5)
print("Rectangle area:", area)

#Question5:
def apply_operation(func, number):
    return func(number)
#Define double function
def double(number):
    return number * 2

#Use apply_operation 
result1 = apply_operation(double, 7)
print("Doubleof 7:", result1)

#Use apply_opperation with square
def square(number):
    return number * number
result2 = apply_operation(square, 3)
print("square of 3:", result2)

