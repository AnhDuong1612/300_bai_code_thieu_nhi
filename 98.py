import math
n = int(input())
def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    count = 0 
    total = 0 
    num = 2
    while count < n:
        if(isPrime(num) and isPrime(num+2)):
            total += num
            count += 1 
        num += 1
    
    return total 
print(solve(n))