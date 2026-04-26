#Question1:
#Create a list
fruits = ["apple", "banana", "orange"]
#Add a fruit 
fruits.append("grape")
#Insert a fruit
fruits.insert(0, "mango")
#Remove a fruit
fruits.remove("banana")
#Print the modifired list
print("Modified fruit list:", fruits)

#Question2:
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
    total = sum(numbers)
average = total / len(numbers)
print("Original numbers:", numbers)
print("squared numbers:", squared_numbers)
print("sum:", total)
print("average:", average)

#Question3:
countries = {"South Africa": "Cape Town", "France": "Paris", "Japan": "Tokyo"}
countries["Germany"] = "Berlin"
countries.pop("France")
print("Modified countries dictionary:", countries)

#Question4:
fruit_colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
print("fruit:", fruit_colors.keys())
print("colors:", fruit_colors.values())
for fruit, color in fruit_colors.items():
    print(fruit, "is", color)
fruit_name = "apple"
if fruit_name in fruit_colors:
    print(fruit_name, "is", fruit_colors[fruit_name])
else:
    print(fruit_name, "not found in dictionary")

