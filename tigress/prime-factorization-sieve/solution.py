class PrimeFactorizer:
    def __init__(self, limit):
        self.limit = limit
        self.spf = list(range(limit + 1))  # smallest prime factor
        
        # Sieve of Eratosthenes to compute SPF
        for i in range(2, int(limit**0.5) + 1):
            if self.spf[i] == i:  # i is prime
                for j in range(i*i, limit + 1, i):
                    if self.spf[j] == j:
                        self.spf[j] = i
    
    def factorize(self, n):
        """Factorize n into prime factors with exponents"""
        if n == 1:
            return [(1, 1)]
        
        factors = {}
        temp = n
        
        while temp > 1:
            factor = self.spf[temp]
            factors[factor] = factors.get(factor, 0) + 1
            temp //= factor
        
        # Convert to sorted list of tuples
        result = sorted(factors.items())
        return result

def solve_prime_factorization():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    numbers = [int(input[i]) for i in range(1, 1 + t)]
    
    max_n = max(numbers) if numbers else 0
    if max_n < 1:
        max_n = 1
    
    factorizer = PrimeFactorizer(max_n)
    results = []
    
    for n in numbers:
        factors = factorizer.factorize(n)
        factor_str = " ".join(f"{p}^{e}" for p, e in factors)
        results.append(factor_str)
    
    return results