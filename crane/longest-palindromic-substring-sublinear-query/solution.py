class LPSQuery:
    def __init__(self, s: str):
        """
        Preprocesses string s in O(n) using Manacher's algorithm.
        """
        self.s = s
        if not s:
            self.longest = ""
            return
        
        # Transform s to handle even-length palindromes
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n  # P[i] = radius of palindrome at i
        C = R = 0  # Center and right boundary
        
        max_len = 0
        center_idx = 0
        
        for i in range(1, n - 1):
            if i < R:
                P[i] = min(R - i, P[2 * C - i])
            # Expand
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            # Update center and right
            if i + P[i] > R:
                C, R = i, i + P[i]
            # Track longest
            if P[i] > max_len:
                max_len = P[i]
                center_idx = i
        
        start = (center_idx - max_len) // 2
        self.longest = s[start:start + max_len]
    

    def query(self) -> str:
        """
        Returns longest palindromic substring in O(1) time.
        For dynamic case, could be O(log n) with heap maintenance.
        """
        return self.longest


def longestPalindromicSubstring(s: str) -> str:
    """
    Wrapper function: preprocesses and returns LPS.
    Time: O(n) preprocessing, O(1) query
    Space: O(n)
    """
    solver = LPSQuery(s)
    return solver.query()
