# Print all numbers from 1 to 20 that are divisible by 3, using range().
def number(n):
    for i in range(1,n+1):
        if i%3 ==0:
            print(i)
    
print(number(100))