def max_subarray(nums):
    """
    Finds maximum sum of contiguous subarray using Kadane's algorithm.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    max_sum = nums[0]  # Global maximum
    current_sum = nums[0]  # Current subarray sum
    
    for i in range(1, len(nums)):
        # Either extend current subarray or start new one
        current_sum = max(nums[i], current_sum + nums[i])
        # Update global maximum
        max_sum = max(max_sum, current_sum)
    
    return max_sum
