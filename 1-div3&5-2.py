sum = 0

n = 1

while (n < 1000):
    
    if n % 15:
        sum = sum + n
    
    elif n % 3:
        sum = sum + n

    elif n % 5:
        sum = sum + n
    
    n = n + 1

print("This is the answer " ,sum) 
