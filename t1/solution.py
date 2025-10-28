from collections import deque, defaultdict
import math

class PrimePathTransformer:

    def __init__(self):
        self.primes = self._generate_primes()
        self.prime_set = set(self.primes)
        self.graph = self._build_graph()
    
    def _generate_primes(self):
        n = 10000
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        
        return [i for i in range(1000, 10000) if sieve[i]]
    
    def _is_prime(self, n):
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
    
    def _is_four_digit_prime(self, n):
        return 1000 <= n <= 9999 and self._is_prime(n)
    
    def _get_neighbors(self, prime):
        neighbors = []
        prime_str = str(prime)
        
        for pos in range(4):  # 4-digit number
            for digit in '0123456789':
                if digit == prime_str[pos]:
                    continue
                # Don't allow leading zero
                if pos == 0 and digit == '0':
                    continue
                
                new_num_str = prime_str[:pos] + digit + prime_str[pos+1:]
                new_num = int(new_num_str)
                
                if new_num in self.prime_set:
                    neighbors.append(new_num)
        
        return neighbors
    
    def _build_graph(self):
        graph = defaultdict(list)
        
        for prime in self.primes:
            graph[prime] = self._get_neighbors(prime)
        
        return graph
    
    def find_shortest_path(self, A, B):
        # Step 1: Validate inputs
        if not self._is_four_digit_prime(A):
            return 'invalid_input', f"Error: {A} is not a 4-digit prime number", []
        
        if not self._is_four_digit_prime(B):
            return 'invalid_input', f"Error: {B} is not a 4-digit prime number", []
        
        if A == B:
            return 'success', f"Shortest path found (length: 1)", [A]
        
        # Step 2: BFS to find shortest path
        visited = set()
        queue = deque()
        parent = {}  # To reconstruct path
        
        visited.add(A)
        queue.append(A)
        parent[A] = None
        
        while queue:
            current = queue.popleft()
            
            # Found target
            if current == B:
                # Reconstruct path
                path = []
                node = B
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path.reverse()
                
                return 'success', f"Shortest path found (length: {len(path)})", path
            
            # Explore all neighbors
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
        
        # No path found
        return 'no_path', f"Error: Cannot generate path from {A} to {B}", []


def prime_path_transformation(A, B):
    transformer = PrimePathTransformer()
    status, message, path = transformer.find_shortest_path(A, B)
    
    print(message)
    if status == 'success' and path:
        print("Path:", " → ".join(map(str, path)))
    return path