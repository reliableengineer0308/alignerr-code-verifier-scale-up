def maxRatioOfThree(nums):
    """
    Optimized O(n²) version using incremental min tracking.
    """
    n = len(nums)
    if n < 3:
        return 0.0
    
    max_ratio = 0.0
    
    # min_prefix[i] = minimum value in nums[0..i]
    min_prefix = nums[:]
    for i in range(1, n):
        min_prefix[i] = min(min_prefix[i-1], nums[i])
    
    
    for k in range(2, n):
        min_product = float('inf')
        # For each j in [1, k-1], min_product candidate is min_prefix[j-1] * nums[j]
        for j in range(1, k):
            left_min = min_prefix[j-1]
            product = left_min * nums[j]
            if product < min_product:
                min_product = product
        ratio = nums[k] / min_product
        max_ratio = max(max_ratio, ratio)
    
    
    return max_ratio
