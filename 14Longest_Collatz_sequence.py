# 14Longest_Collatz_sequence.py
# unsolved

def collatz_nums(n):
    counter = 1
    print(int(n), counter)
    while n != 1:
        counter += 1
        if n % 2 == 0:
            n /= 2
        elif n % 2 != 0:
            n = (3 * n) + 1
        print(counter, int(n))
    return counter
    
    
def pow_of_2(n):
    if n % 2 != 0:
        return False

    while True:
        if n == 1:
            return True
        elif n % 2 == 0: 
            n = n // 2
            continue
        elif n % 2 != 0:
            return False




list_of_counters = []
for i in range(1,1e6):
    if not pow_of_2(i):
        continue

    