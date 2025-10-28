from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    
    result = []
    dq = deque()  # store indices
    
    for i in range(len(nums)):
        # Remove indices that are out of current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result when window size is reached
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result