'''

import string

first_name = "priscilla"
print(type(first_name))
my_school = "Good Hope School"
print(string.ascii_letters)
print(repr(string.whitespace))
my_grades = (10, 9, 8, 10, 10)
print(len(my_grades))
for i in my_grades:
    print(i)

all_grades = (
    (4, 6, 8),
    (2, 7, 5),
    (1, 3, 0)
)
for grade in all_grades:
    for i in grade:
        print(i)
    print("\n")
print(all_grades[0][1])
print(all_grades[1][2])

name = "Priscilla"
name = "Priscilla" * 3
print(name)

a = ("m", "n", "o")
b = ["d", "f", "r"]
b[0] = "w"
print(b)

c = "hello"
d = b"hello"
print(type(c), type(d))

print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord("z"))
print(chr(91))



my_name = "Abena"
print(list(my_name))

raw_version = b"Abena"
print(list(raw_version))

grining_face = "😀"
encode_grining_face = grining_face.encode("utf-8")
print(list(encode_grining_face))

q = "Frank is playing ⚽"
encode_q = q.encode("utf-8")
print(list(encode_q))
print(encode_q.decode("utf-8"))

names = ["abena", "kojo", "pp"]
names.insert(1, "maa")
for name in names:
    print(name)

    add = 0 
grades = [20, 30, 40, 50, 60]
for grade in grades:
    add = add + grade
print(add)


error_margin = [0.16, 0.22, -0.8, 7.2, 22.1]
result = 0
for i in error_margin:
    result = (result + i)
average = result / len(error_margin)
print(f"The average is {result}")

byte_data = bytes([97, 98, 101, 110, 97])
print(byte_data)

myself_byte_data = b"abena"
print(list(myself_byte_data))

string_vowels = "aeiou"
list_vowels = list(string_vowels)
print(list_vowels) # ['a', 'e', 'i', 'o', 'u']
sentence = "I am going home"
print(list(sentence))

# slicing
friuts = ["mango", "apple", "banana", "orange", "kiwi"]
print(friuts[0:3])
print(friuts[1:]) # friuts[1:len(friuts)]
print(friuts[:])
print(friuts[:3])
print(friuts[1:4])
print(friuts[0:5:2])

# Negative slicing or reversal order
print(friuts[-3:])
print(friuts[-3:0]) # empty
print(friuts[::-1]) # reverses the entire list
print(friuts[1:4:-1]) # empty
print(friuts[-1:-4:-1])
print(friuts[-5:-2:])
print(friuts[-5:-2:1])
print(friuts[-5:-2:-1])
print(friuts[-3:-6:-1])
print(friuts[-3::-1])
print(friuts[2::-1])
print(friuts[-4:-1:1])
print(friuts[1:4:1])
print(friuts[3:0:-1])
print(friuts[-2:-5:-1])



# loop
# for loop
a = range(1, 36)
print(list(a))

for num in range(10, 41):
   print(num, end=",")

# while loop
x = 0
while x < 16:
    print(x)
    x = x + 1

    def testCar(cars):  

    for car in cars:
        if car == "bmw":
          print(f"I have a {car.upper()}")
        else:
          print(f"I have a {car}")


cars = ["audi", "bmw", "subaru", "toyota"]
testCar(cars)


def numbers():
   for num in range(1, 20):
        if num % 3 == 0 and num % 5 == 0:
           print("FizzBuzz-", num)
        elif num % 3 == 0:
            print("Fizz-", num)
        elif num % 5 == 0:
           print("Buzz-", num)
          

numbers()

def even_numbers_assignment():
    numbers = 2
    while numbers <= 100:
        if numbers % 2 == 0:
            print("Even numbers ",numbers)
        numbers += 1

even_numbers_assignment()

def counting_backwards():
    counting_numbers = 10
    while counting_numbers >= 1:
        print("backwarss counting", counting_numbers)
        counting_numbers -= 1
counting_backwards()

def indexing_fruits():
    fruits = [
        "mango", "apple", "pawpaw", "guava", "orange", "banana", "kiwi", "grapes"
    ]

    for index in range(0, len(fruits)):
        print(fruits[index])

indexing_fruits()



# Dictionary
my_profile =  {
    "Firstname": "Abena",
    "Lastname": "Aboagye",
    "Age": 19,
    "Single": True
}
print(type(my_profile))
print(my_profile)

my_self = {
    "name": "Abena Priscilla",
    "school": "Good hope",
    "best food": ["banku", "Kenkey"],
    "is_married": False
}

print(my_self["school"])
print(my_self.get("is_married"))
# print(my_self["surname"])  Error
print(my_self.get("surname")) # None
print(my_self.get("surname", "Aboagye"))
my_self["best_friend"] = "Me"
print(my_self.items()) 
print(my_self.keys())
print(my_self.values())
my_self.clear()
print(my_self)
deleted_value = my_self.pop("best food")
print(my_self)
my_self.popitem()
print(my_self)

for a, b in my_self.items():
    print(f"The key = {a}, the value = {b}")


def multiplyBy2(x):
    print(x * 2)
m = multiplyBy2(7)
print(f"m = {m}")
'''

# Arguments
def printName(*args):
    print(type(args))
    print(args[2])
printName("Priscilla", "Abena", "Aboagye")

# Keyword arguments
def showAll(**kwargs):
    print(type(kwargs))
    print(kwargs)
showAll(firstName="abena", age=11, pin=2015)

class User:
    def __init__(self, first_name, last_name, age, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password

    def introduction(self):
        print(f"My name is {self.first_name} {self.last_name}. I am {self.age} years old. My password is {self.password}")

user1 = User("Abena", "Paa", 2, "iwn38r74u49")
user2 = User("Ben", "Kojo", 22, "1ie8ejd")

print(user1.introduction())

class Animal:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def make_sound(self, the_animal_sound):
        return f"The Animal {self.name} makes the sound {the_animal_sound}"
    
    def isLoyal(self):
        if self.type == "domesticated":
            return "True it is loyal"
        else:
            return "False it is not loyal"
        
cat = Animal("Kitty cat", "domesticated")
print(cat.type)
print(cat.make_sound("meoww"))