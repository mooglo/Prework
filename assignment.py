# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print("hello_" + user_name + "!")
hello_name('USERNAME')

# Question 2 
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for m in range(1,101):
        if m % 2==1:
          print(m)

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    return max (a_list)
print(max_num_in_list([5,6,7,8,9,10]))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_a_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False
print(is_a_leap_year(1996))
print(is_a_leap_year(2000))
print(is_a_leap_year(2002))
print(is_a_leap_year(2004))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
def is_consecutive(a_list):
    if not a_list:
        return False
    if a_list [-1] - a_list[0] == len(a_list) - 1:
        for m in range(len(a_list)- 1):
            if a_list[m+1] - a_list[m] != 1:
                return False
        return True
    else:
        return False
numbers = [2,3,4,5,6,7]
print(is_consecutive(numbers))
numbers = [1,2,4,5]
print(is_consecutive(numbers))