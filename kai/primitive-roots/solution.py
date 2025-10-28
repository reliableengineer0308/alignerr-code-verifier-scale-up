class PrimitiveRootFinder:
    def __init__(self, limit):
        self.limit = limit
        self.spf = list(range(limit + 1))
        self._sieve()
    
    def _sieve(self):
        for i in range(2, int(self.limit**0.5) + 1):
            if self.spf[i] == i:
                for j in range(i*i, self.limit + 1, i):
                    if self.spf[j] == j:
                        self.spf[j] = i
    
    def _factorize(self, n):
        factors = set()
        temp = n
        while temp > 1:
            p = self.spf[temp]
            factors.add(p)
            while temp % p == 0:
                temp //= p
        return factors
    
    def _is_primitive_root(self, g, p, factors):
        """Check if g is a primitive root modulo p"""
        for q in factors:
            if pow(g, (p-1) // q, p) == 1:
                return False
        return True
    
    def find_smallest_primitive_root(self, p):
        if p == 2:
            return 1
        
        factors = self._factorize(p-1)
        
        for g in range(2, p):
            if self._is_primitive_root(g, p, factors):
                return g
        
        return -1  # Should not happen for primes

def solve_primitive_roots():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    primes = [int(input[i]) for i in range(1, 1 + t)]
    
    max_p = max(primes) if primes else 2
    root_finder = PrimitiveRootFinder(max_p)
    results = []
    
    for p in primes:
        result = root_finder.find_smallest_primitive_root(p)
        results.append(str(result))
    
    return results