import math
import random

def is_prime(n, k=5):
    """Miller-Rabin primality test"""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as d*2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    def check_composite(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        if check_composite(a):
            return False
    return True

def pollard_rho(n):
    """Find a non-trivial factor of n using Pollard's Rho algorithm"""
    if n % 2 == 0:
        return 2
    
    if is_prime(n):
        return n
    
    def f(x, c, n):
        return (x * x + c) % n
    
    while True:
        c = random.randint(1, n - 1)
        x = random.randint(0, n - 1)
        y = x
        
        while True:
            x = f(x, c, n)
            y = f(f(y, c, n), c, n)
            d = math.gcd(abs(x - y), n)
            
            if d == n:
                break
            if d > 1:
                return d

def solve_pollard_rho():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    numbers = [int(input[i]) for i in range(1, 1 + t)]
    
    results = []
    
    for n in numbers:
        if n == 4:
            results.append("2")
        else:
            factor = pollard_rho(n)
            results.append(str(factor))
    
    return results