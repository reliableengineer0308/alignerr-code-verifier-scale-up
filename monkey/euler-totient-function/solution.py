class EulerTotient:
    def __init__(self, limit):
        self.limit = limit
        self.phi = list(range(limit + 1))
        self.computed = False
    
    def compute_phi(self):
        """Compute Euler's Totient function for all numbers up to limit"""
        if self.computed:
            return
        
        for i in range(2, self.limit + 1):
            if self.phi[i] == i:  # i is prime
                for j in range(i, self.limit + 1, i):
                    self.phi[j] -= self.phi[j] // i
        
        self.computed = True
    
    def get_phi(self, n):
        """Get φ(n)"""
        if not self.computed:
            self.compute_phi()
        return self.phi[n]

def solve_euler_totient():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    numbers = [int(input[i]) for i in range(1, 1 + t)]
    
    max_n = max(numbers) if numbers else 0
    if max_n < 1:
        max_n = 1
    
    totient_calculator = EulerTotient(max_n)
    results = []
    
    for n in numbers:
        result = totient_calculator.get_phi(n)
        results.append(str(result))
    
    return results