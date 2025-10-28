def solve(data):
    """
    Find the maximum sum of non-adjacent elements in the array.
    Using the standard House Robber algorithm.
    """
    if not data:
        return 0
    
    n = len(data)
    if n == 1:
        return max(0, data[0])
    
    # Two variables to track the maximum sums
    prev2 = 0  # max sum up to i-2
    prev1 = max(0, data[0])  # max sum up to i-1
    
    for i in range(1, n):
        # Either take current + prev2, or skip current and take prev1
        current = max(prev1, data[i] + prev2)
        prev2 = prev1
        prev1 = current
    
    return prev1