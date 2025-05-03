'''

Write a for loop that prints all the even numbers from 1 to 20.

Use a for loop to calculate the sum of all the numbers from 1 to 50.

Write a for loop that prints each character in the string "SwiftWay".

Given the list fruits = ["apple", "banana", "cherry", "date"], write a for loop to print each fruit in uppercase.

Create a for loop that prints the square of numbers from 1 to 10.

Write a for loop that counts down from 10 to 1.

Use a for loop to iterate through the list numbers = [3, 7, 9, 2, 5] and print only the numbers greater than 5.

Write a for loop that prints the multiplication table of 3 from 1 to 12.

Given a list of words, write a for loop that prints only the words with more than 4 letters.
Example: words = ["hi", "hello", "world", "yes", "Python"]

Write a for loop that adds the numbers in a list and prints the result.
Example: nums = [4, 8, 15, 16, 23, 42]

'''

# Question 1
def prints_even_numbers():
    numbers = 0

    for num in range(1,21):
       if num % 2 == 0:
           print("Even numbers: ", num)
       numbers += 1
prints_even_numbers()

# Question 2

