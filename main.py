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

'''

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