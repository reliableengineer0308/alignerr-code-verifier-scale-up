import bisect

def length_of_lis(nums):
    """
    Returns the length of the longest strictly increasing subsequence.
    Time: O(n log n), Space: O(n)
    """
    if not nums:
        return 0
    
    tails = []  # tails[i] = smallest tail of LIS of length i+1
    
    for num in nums:
        # Find the leftmost position where num can be inserted
        pos = bisect.bisect_left(tails, num)
        
        if pos == len(tails):
            # num is larger than all elements in tails → extend LIS
            tails.append(num)
        else:
            # Replace the element at pos with num (to maintain smallest tail)
            tails[pos] = num
    
    
    return len(tails)
