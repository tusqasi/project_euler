# 6sumsquaredifference.py
# Solved
# 25164150
def sum_of_nums_till(n):
    return ( (n*(n + 1)) / 2)


def sum_of_sqrs_of_nums_tills(n):
    return ( (n*(n + 1)*(2*n + 1)) / 6)

num = 100

print(sum_of_nums_till(num)**2 - sum_of_sqrs_of_nums_tills(num))
