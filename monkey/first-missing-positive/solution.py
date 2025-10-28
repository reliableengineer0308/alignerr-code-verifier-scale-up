def first_missing_positive(nums: list[int]) -> int:
    """
    Finds the smallest missing positive integer in O(n) time and O(1) space.
    
    Uses in-place array modification: treats indices as hash keys.
    Places each valid number x in range [1, n] at index x-1.
    Then scans to find first mismatch.
    
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    
    # Step 1: Place each number in its correct position if possible
    for i in range(n):
        # While current number is in valid range [1, n] and not in correct place
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] to its correct index: nums[i]-1
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
    
    
    # Step 2: Scan for first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1  # i+1 is the first missing
    
    
    # If all 1..n are present, missing is n+1
    return n + 1
