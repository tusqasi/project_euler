# 14Longest_Collatz_sequence.py
# solved
# 837799

def collatz_nums(n):
    copy = n
    counter = 1
    while n != 1:
        counter += 1
        if n % 2 == 0:
            n /= 2
        elif n % 2 != 0:
            n = (3 * n) + 1
    return counter, copy
    
    



list_of_counters = []
list_of_nums = []
for i in range(1, int(1e6)):
    num = collatz_nums(i)
    list_of_counters.append(num[0])
    list_of_nums.append(num[1])

lisd = dict()
    
