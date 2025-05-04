# Question 1
def prints_even_numbers():
    numbers = 0

    for num in range(1,21):
       if num % 2 == 0:
           print("Even numbers: ", num)
       numbers += 1
prints_even_numbers()

# Question 2
def sum_of_numbers():
    total_numbers = 0
    for num in range(1, 51):
        total_numbers = total_numbers + num
        print(total_numbers)
    total_numbers += 1 
sum_of_numbers()

# Question 3
def prints_character(E):
    for i in E:
        print(i)

prints_character("SwiftWay") 

# Question 4
fruits = [
    "apple", "banana", "cherry", "date"
]
for fruit in fruits:
    print(fruit.upper())

# Question 5
numbers = range(1, 11)
for number in numbers:
    print(pow(number, 2))

# Question 6

