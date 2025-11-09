'''
words = ["apple", "banana", "cherry"]

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


def anagram_solution1(s1,s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
    while pos2 < len(a_list) and not found:
        if s1[pos1] == a_list[pos2]:
            found = True
        else:
            pos2 = pos2 + 1
        if found:
            a_list[pos2] = None
        else:
            still_ok = False
        pos1 = pos1 + 1
    return still_ok

print(anagram_solution1('abcd','dcba'))

import time
def sum_of_numbers(n):
    start = time.time()
    sum_num = 0
    for num in range(1, n+1):
        sum_num += num
    end = time.time()
    print(f"the sum is {sum_num}. It took {end-start:.10f} seconds")

sum_of_numbers(1000000000)


# anagram solution 2
def anagram_solution(s1, s2):
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    post = 0
    matches = True

    while post < len(s1) and matches:
        if a_list1[post] == a_list2[post]:
            post += 1
        else:
            matches = False
    return matches
print(anagram_solution("heart", "earth"))
'''

def anagram_solution3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i])- ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])- ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True

    while j < 0 and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False
    return still_ok

print(anagram_solution3("heart", "earth"))