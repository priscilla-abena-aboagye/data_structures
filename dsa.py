words = ["apple", "banana", "cherry"]
'''
convert to uppercase

words_upper = []
for word in words:
    words_upper.append(word.upper())
print(words_upper)

list comprehension
words_upper = [word.upper() for word in words]
print(words_upper)

all_nums = [8, 0, -38, 2, -59.5, -9, 2, 11, 4, -2]

postive_nums = [num for num in all_nums if num >= 0]
print(postive_nums)

exceptions are types of runtime errors that cause the program to terminate
try statement handles a raised execption

enter a num convert to int not a number print something else print ...

number = input("Enter a number: ")
try:
    number = int(number)
    print(f"You entered {number}")
except:
    print("That's not a valid number")

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num} / {self.den}"
    
    def show(self):
        print(f"the numerator is {self.num} and the denominator is {self.den}")

my_fraction = Fraction(3, 5)
print(my_fraction)
my_fraction.show()

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z =z

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z 
        return Point(new_x, new_y, new_z)
    
    def __mul__(self, other):
        new_x = self.x * other.x 
        new_y = self.y * other.y 
        new_z = self.z * other.z 
        return Point(new_x, new_y, new_z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
point1 = Point(2, 3, 4)
point2 = Point(5, 6, 7)
new_point = point1 + point2
print(new_point)
'''
import time
def sum_of_n(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum, end-start
print(sum_of_n(10))

def sum_of_n(n):
    start = time.time()

    the_sum = sum([i for i in range(1, n+1)])
    end = time.time()
    return the_sum, end-start
print(sum_of_n(10))