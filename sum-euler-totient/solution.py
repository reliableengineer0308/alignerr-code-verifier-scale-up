class TotientSum:
    def __init__(self, limit):
        self.limit = limit
        self.phi = list(range(limit + 1))
        self.sum_phi = [0] * (limit + 1)
        self._sieve()
    
    def _sieve(self):
        # Compute phi using sieve
        for i in range(2, self.limit + 1):
            if self.phi[i] == i:  # i is prime
                for j in range(i, self.limit + 1, i):
                    self.phi[j] -= self.phi[j] // i
        
        # Compute prefix sums
        self.sum_phi[0] = 0
        for i in range(1, self.limit + 1):
            self.sum_phi[i] = self.sum_phi[i-1] + self.phi[i]
    
    def get_sum(self, n):
        """Get sum of φ(1) to φ(n)"""
        return self.sum_phi[n]

def solve_totient_sum():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    numbers = [int(input[i]) for i in range(1, 1 + t)]
    
    max_n = max(numbers) if numbers else 1
    totient_calculator = TotientSum(max_n)
    results = []
    
    for n in numbers:
        result = totient_calculator.get_sum(n)
        results.append(str(result))
    
    return results