def longest_consecutive(nums: list[int]) -> int:
    """
    Returns the length of the longest consecutive elements sequence in O(n) time.
    
    Uses hash set for O(1) lookups. Only starts counting from numbers that are 
    the beginning of a sequence (i.e., num-1 is not present).
    
    Time: O(n), Space: O(n)
    """
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in nums:
        # Only start counting if 'num' is the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count consecutive numbers: num+1, num+2, ...
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length
