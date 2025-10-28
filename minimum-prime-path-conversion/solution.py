from collections import deque
import math

class PrimePathFinder:
    def __init__(self):
        self.primes = self.generate_4digit_primes()
        self.graph = self.build_graph()
    
    def generate_4digit_primes(self):
        """Generate all 4-digit prime numbers (1000 to 9999)"""
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
        primes = []
        for num in range(1000, 10000):
            if is_prime(num):
                primes.append(num)
        return primes
    
    def are_connected(self, a, b):
        """Check if two primes differ by exactly one digit"""
        str_a = str(a)
        str_b = str(b)
        diff_count = 0
        for i in range(4):
            if str_a[i] != str_b[i]:
                diff_count += 1
        return diff_count == 1
    
    def build_graph(self):
        """Build graph where edges connect primes differing by one digit"""
        graph = {}
        prime_set = set(self.primes)
        
        for prime in self.primes:
            graph[prime] = []
            str_prime = str(prime)
            
            # Try changing each digit position
            for pos in range(4):
                for digit in '0123456789':
                    if digit == str_prime[pos]:
                        continue
                    
                    # Don't create numbers starting with 0
                    if pos == 0 and digit == '0':
                        continue
                    
                    new_str = str_prime[:pos] + digit + str_prime[pos+1:]
                    new_num = int(new_str)
                    
                    if new_num in prime_set and new_num != prime:
                        graph[prime].append(new_num)
        
        return graph
    
    def find_min_steps(self, start, end):
        """Find minimum steps from start to end using BFS"""
        if start == end:
            return 0
        
        if start not in self.graph or end not in self.graph:
            return -1
        
        visited = set()
        queue = deque([(start, 0)])  # (current_number, steps)
        visited.add(start)
        
        while queue:
            current, steps = queue.popleft()
            
            for neighbor in self.graph[current]:
                if neighbor == end:
                    return steps + 1
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return -1

def solve_prime_path():
    import sys
    input = sys.stdin.read().split()
    
    T = int(input[0])
    results = []
    path_finder = PrimePathFinder()
    
    idx = 1
    for _ in range(T):
        A = int(input[idx])
        B = int(input[idx + 1])
        idx += 2
        
        steps = path_finder.find_min_steps(A, B)
        if steps == -1:
            results.append("Impossible")
        else:
            results.append(str(steps))
    
    return results