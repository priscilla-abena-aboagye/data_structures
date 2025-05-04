'''
# Question 1
def prints_even_numbers():
    numbers = 0

    for num in range(1,21):
       if num % 2 == 0:
           print("Even numbers: ", num)
       numbers += 1
prints_even_numbers()
print("----------------------------")

# Question 2
def sum_of_numbers():
    total_numbers = 0
    for num in range(1, 51):
        total_numbers = total_numbers + num
        print(total_numbers)
    total_numbers += 1 
sum_of_numbers()
print("--------------------------------")

# Question 3
def prints_character(E):
    for i in E:
        print(i)

prints_character("SwiftWay") 
print("-------------------------------")

# Question 4
fruits = [
    "apple", "banana", "cherry", "date"
]
for fruit in fruits:
    print(fruit.upper())
print("-------------------------")

# Question 5
numbers = range(1, 11)
for number in numbers:
    print(pow(number, 2))
print("------------------------")

# Question 6
backwards = list(range(11))
counting_backwards = backwards[::-1]
for back in counting_backwards:
    print(back)
print("------------------------")
'''

# Question 7
list_of_numbers= [3, 7, 9, 2, 5]
for num in list_of_numbers:
    if num > 5:
        print(num)
print("---------------------------")

# Question 8
mul_of_num = range(1, 13)
for num in mul_of_num:
    if num % 3 == 0:
        print(num)
