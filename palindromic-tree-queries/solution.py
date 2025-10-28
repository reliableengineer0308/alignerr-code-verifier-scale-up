import sys

class SimplePalindromicSolver:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.palindromes = set()
        
        # Find all distinct palindromic substrings using expansion
        for i in range(self.n):
            # Odd length palindromes
            self.expand_from_center(i, i)
            # Even length palindromes
            self.expand_from_center(i, i + 1)
        
        # Convert to sorted list
        self.palindrome_list = sorted(self.palindromes)
        
        # Count occurrences by finding all starting positions
        self.counts = self.count_occurrences_by_positions()
        
        # Combine into list of tuples
        self.palindrome_data = list(zip(self.palindrome_list, self.counts))
    
    def expand_from_center(self, left, right):
        while left >= 0 and right < self.n and self.s[left] == self.s[right]:
            self.palindromes.add(self.s[left:right+1])
            left -= 1
            right += 1
    
    def count_occurrences_by_positions(self):
        """Count occurrences by finding all unique starting positions"""
        counts = []
        for pal in self.palindrome_list:
            # Find all starting positions of this palindrome
            positions = set()
            start = 0
            while True:
                pos = self.s.find(pal, start)
                if pos == -1:
                    break
                positions.add(pos)  # Use set to avoid duplicates
                start = pos + 1
            
            counts.append(len(positions))
        return counts
    
    def get_count(self):
        return len(self.palindrome_list)
    
    def get_longest(self):
        if not self.palindrome_list:
            return ""
        return max(self.palindrome_list, key=len)
    
    def get_kth_freq(self, k):
        if 1 <= k <= len(self.palindrome_data):
            return self.palindrome_data[k-1][1]
        return 0
    
    def get_kth_palindrome(self, k):
        if 1 <= k <= len(self.palindrome_data):
            return self.palindrome_data[k-1][0]
        return ""

def solve_palindromic_tree():
    input = sys.stdin.read().splitlines()
    if not input:
        return []
    
    s = input[0].strip()
    q = int(input[1])
    
    solver = SimplePalindromicSolver(s)
    
    results = []
    
    for i in range(2, 2 + q):
        query = input[i].split()
        if query[0] == "COUNT":
            results.append(str(solver.get_count()))
        elif query[0] == "LONGEST":
            results.append(solver.get_longest())
        elif query[0] == "FREQ":
            k = int(query[1])
            results.append(str(solver.get_kth_freq(k)))
        else:  # KTH
            k = int(query[1])
            results.append(solver.get_kth_palindrome(k))
    
    return results