def longest_repeating_substring(s: str) -> int:
    """
    Find the length of the longest substring that appears at least twice in s.
    Uses binary search + rolling hash (Rabin-Karp) for efficiency.
    """
    if len(s) <= 1:
        return 0

    n = len(s)
    base = 26
    mod = 10**9 + 7

    # Precompute powers of base
    power = [1] * n
    for i in range(1, n):
        power[i] = (power[i-1] * base) % mod

    def get_hash(sub: str) -> int:
        h = 0
        for ch in sub:
            h = (h * base + (ord(ch) - ord('a'))) % mod
        return h

    def has_repeating(L: int) -> bool:
        """Check if any substring of length L appears at least twice."""
        if L == 0:
            return True
        seen = set()
        # Compute hash of first window
        window_hash = get_hash(s[:L])
        seen.add(window_hash)

        # Rolling hash for subsequent windows
        for i in range(1, n - L + 1):
            # Remove leftmost char, add rightmost
            window_hash = (window_hash - (ord(s[i-1]) - ord('a')) * power[L-1]) % mod
            window_hash = (window_hash * base + (ord(s[i+L-1]) - ord('a'))) % mod
            # Ensure non-negative
            window_hash = window_hash % mod

            if window_hash in seen:
                return True
            seen.add(window_hash)
        return False

    # Binary search on length
    low, high = 1, n - 1
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if has_repeating(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer
