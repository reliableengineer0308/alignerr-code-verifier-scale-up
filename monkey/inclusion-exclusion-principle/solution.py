def inclusion_exclusion(n, primes):
    """
    Count numbers from 1 to n divisible by at least one prime in the list
    using inclusion-exclusion principle
    """
    k = len(primes)
    total = 0
    
    # Generate all non-empty subsets
    for i in range(1, 1 << k):
        product = 1
        count = 0
        
        for j in range(k):
            if i & (1 << j):
                product *= primes[j]
                count += 1
        
        if count % 2 == 1:
            total += n // product
        else:
            total -= n // product
    
    return total

def solve_inclusion_exclusion():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input[idx])
        k = int(input[idx + 1])
        idx += 2
        
        primes = list(map(int, input[idx:idx + k]))
        idx += k
        
        result = inclusion_exclusion(n, primes)
        results.append(str(result))
    
    return results