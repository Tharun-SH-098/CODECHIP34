fruits=["apple","banana","orange"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])

fruits[1]="grape"
print(fruits)

fruits.append("kiwi")
print(fruits)

fruits.insert(1,"mango")
print(fruits)

fruits.remove("orange")
print(fruits)

popped_fruit=fruits.pop()
print(popped_fruit)
print(fruits)

numbers=[1,2,3,4,5,6,7,8,9,10]
sliced_numbers=numbers[2:6]
print(sliced_numbers)

even_numbers=numbers[1::2]
print(even_numbers)

print(len(fruits))

print(len(numbers))

for fruit in fruits:
    print(fruit)

for number in numbers:
    print(number)
