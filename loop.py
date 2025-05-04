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
