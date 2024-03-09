# Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    """Display a greeting"""
    print("Hello, " + user_name.title() + "!")

hello_name('username')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds(num):
    for i in range(1, num+1):
        if i % 2 != 0:
            print(i,end=",")

n = 100
first_odds(n)      

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
            return max
        
print(max_num_in_list([1, 8, 4, -6, 0]))        


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if divmod(a_year, 4)[1] == 0 and (divmod(a_year, 100)[1] != 0 or divmod(a_year, 400)[1] == 0):
        return True
    else:
        return False

print(is_leap_year(2018))
print(is_leap_year(2000))
print(is_leap_year(2024))     


               
# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    if not a_list:
        return False
    
    min_num = min(a_list)
    max_num = max(a_list)

    return max_num - min_num == len(a_list) - 1

print(is_consecutive([5, 6, 7, 8, 9, 10]))
print(is_consecutive([1, 3, 5, 6, 8]))