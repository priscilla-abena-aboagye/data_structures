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
'''
# to move from ADT to Data structure it is called class 
class Stack:
    def __init__(self):
        self.my_stack = []  # top is the end and the base is the beginning of the list [base   top]

    def push(self, item):
        self.my_stack.append(item) # to add items 

    def pop(self):
        return self.my_stack.pop() # to remove the top
    
    def peek(self):
        return self.my_stack[-1] # returns the top element
    
    def is_empty(self):
        return len(self.my_stack) == 0 # checks if it is empty
    
    def size(self):
        return len(self.my_stack) # returns the size of the stack

'''    
shoe_stack = Stack()
print(shoe_stack.is_empty())
shoe_stack.push(4)
shoe_stack.push(32)
print(shoe_stack.peek())
print(shoe_stack.size())
print(shoe_stack.is_empty())
shoe_stack.push("Nike")
shoe_stack.pop()
shoe_stack.pop()
print(shoe_stack.size())

def matches(open, close): # top ( symbol )
    opens = "({["
    closes = ")}]"
    return opens.index(open) == closes.index(close)

def bracket_check(bracket): # checking if all brackets are closed  '((()))'
    s = Stack() # creates a new stack (((
    balanced = True
    index = 0

    while index < len(bracket) and balanced:# index = 3 len= 6
        symbol = bracket[index] # )

        if symbol in "({[":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False # if it is empty break the code 
            else:
                top = s.pop() # remove one of the bracket if it is ) top = (
                if not matches(top, symbol): # checks the matches function
                    balanced = False

        index += 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False
    
print(bracket_check('((()))'))
print(bracket_check('(()'))
print(bracket_check('{{([][])}()}'))
print(bracket_check('[{()]'))


def divide_by_2(number): # 42
    remainder_stack = Stack() # 0, 1, 0, 1, 0, 1

    while number > 0:
        remainder = number % 2 # 2 % 2 = 0
        remainder_stack.push(remainder)
        number = number // 2 # 0

        string_remainder = "" # "1", "0", "1", "0", "1", "0"

    while not remainder_stack.is_empty():
        string_remainder += str(remainder_stack.pop())

    return string_remainder
print(divide_by_2(42))
'''

def base_convertor(number, base): # 25, 16
    digits = "0123456789ABCDEF"
    remainder_stack = Stack() # 9, 1

    while number > 0: # 1
        remainder = number % base # 9
        remainder_stack.push(remainder)
        number = number // base # 1

    new_string ="" # 1, 9
    while not remainder_stack.is_empty(): # True
        new_string += digits[remainder_stack.pop()] # digits[1]

    return new_string
print(base_convertor(25, 8))
print(base_convertor(256, 16)) 
print(base_convertor(26, 26))

