class PrimeSieve:
    def __init__(self, limit):
        self.limit = limit
        self.is_prime = None
        self.primes = None
    
    def generate_primes(self):
        """Generate all primes up to limit using Sieve of Eratosthenes"""
        if self.is_prime is not None:
            return
        
        self.is_prime = [True] * (self.limit + 1)
        self.is_prime[0] = self.is_prime[1] = False
        
        for i in range(2, int(self.limit**0.5) + 1):
            if self.is_prime[i]:
                for j in range(i*i, self.limit + 1, i):
                    self.is_prime[j] = False
        
        self.primes = [i for i in range(2, self.limit + 1) if self.is_prime[i]]
    
    def get_primes_up_to(self, n):
        """Get all primes up to n (n <= limit)"""
        if self.primes is None:
            self.generate_primes()
        
        # Find the index where primes exceed n
        result = []
        for prime in self.primes:
            if prime <= n:
                result.append(prime)
            else:
                break
        
        return result

def solve_prime_generation():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    numbers = [int(input[i]) for i in range(1, 1 + t)]
    
    max_n = max(numbers) if numbers else 0
    if max_n < 2:
        max_n = 2
    
    sieve = PrimeSieve(max_n)
    results = []
    
    for n in numbers:
        primes = sieve.get_primes_up_to(n)
        result_str = " ".join(map(str, primes))
        results.append(result_str)
    
    return results