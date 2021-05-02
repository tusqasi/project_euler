# 20factorial_digit_sum.py
# started

def factorial_of(n):
    factorial = 1
    for i in range(2,n+1):
        factorial *= i
    return factorial

def sum_of_digits(n):
    add_to = 0
    the_num = str(n)
    for i in the_num:
        add_to += int(i)
    return add_to

# testing code

print(sum_of_digits(factorial_of(100)))