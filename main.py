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

'''
error_margin = [0.16, 0.22, -0.8, 7.2, 22.1]
result = 0
for i in error_margin:
    result = (result + i)
average = result / len(error_margin)
print(f"The average is {result}")
