def solve(data):
    """
    Find the length of the longest increasing subsequence using optimized O(n log n) approach.
    """
    if not data:
        return 0
    
    n = data[0]
    if n == 0:
        return 0
    
    nums = data[1:1+n]
    
    # tails array - stores the smallest tail of all increasing subsequences of length i+1
    tails = []
    
    for num in nums:
        # Binary search to find the position to replace
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If num is larger than all elements in tails, append it
        if left == len(tails):
            tails.append(num)
        else:
            # Replace the element at left position
            tails[left] = num
    
    return len(tails)