class PrimeFactorCounter:
    def __init__(self, limit):
        self.limit = limit
        self.omega = [0] * (limit + 1)  # number of distinct prime factors
        self._sieve()
    
    def _sieve(self):
        # Sieve to compute omega (number of distinct prime factors)
        for i in range(2, self.limit + 1):
            if self.omega[i] == 0:  # i is prime
                for j in range(i, self.limit + 1, i):
                    self.omega[j] += 1
    
    def count_exactly_k_factors(self, n, k):
        """Count numbers ≤ n with exactly k distinct prime factors"""
        count = 0
        for i in range(1, n + 1):
            if self.omega[i] == k:
                count += 1
        return count

def solve_prime_factors_count():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    
    # Find maximum N for precomputation
    max_n = 0
    temp_idx = idx
    for _ in range(t):
        n = int(input[temp_idx])
        max_n = max(max_n, n)
        temp_idx += 2
    
    if max_n > 0:
        counter = PrimeFactorCounter(max_n)
        results = []
        
        for _ in range(t):
            n = int(input[idx])
            k = int(input[idx + 1])
            idx += 2
            
            count = 0
            for i in range(1, n + 1):
                if counter.omega[i] == k:
                    count += 1
            results.append(str(count))
    else:
        results = []
    
    return results