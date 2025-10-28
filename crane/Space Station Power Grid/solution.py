def solve(data):
    n = data[0]
    power = data[1:1 + n]
    
    if n == 0:
        return 0
    if n == 1:
        return power[0]
    if n == 2:
        return max(power[0], power[1])
    
    def linear_rob(nums):
        """Solve the linear version (non-circular) of the problem"""
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # DP: dp[i] represents maximum sum up to index i without taking adjacent elements
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            # Either skip current element (take dp[i-1]) or take current element + dp[i-2]
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
    
    # Case 1: Include first node, exclude last node
    case1 = linear_rob(power[:-1])
    
    # Case 2: Exclude first node, include last node  
    case2 = linear_rob(power[1:])
    
    return max(case1, case2)