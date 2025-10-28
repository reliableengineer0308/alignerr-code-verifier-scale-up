def find_kth_sorted_arrays(nums1, nums2, k):
    """
    Find k-th smallest element in two sorted arrays using binary search
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        return find_kth_sorted_arrays(nums2, nums1, k)
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        # Partition position in nums1
        i = (left + right) // 2
        # Partition position in nums2
        j = k - i
        
        # Handle boundary cases
        nums1_left = nums1[i-1] if i > 0 else float('-inf')
        nums1_right = nums1[i] if i < m else float('inf')
        nums2_left = nums2[j-1] if j > 0 else float('-inf')
        nums2_right = nums2[j] if j < n else float('inf')
        
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            # Found the correct partition
            return max(nums1_left, nums2_left)
        elif nums1_left > nums2_right:
            # Too many elements from nums1, move left
            right = i - 1
        else:
            # Too few elements from nums1, move right
            left = i + 1
    
    return 0

def solve_kth_element():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for case_num in range(1, t + 1):
        m = int(input[idx])
        n = int(input[idx + 1])
        k = int(input[idx + 2])
        idx += 3
        
        nums1 = []
        for i in range(m):
            nums1.append(int(input[idx]))
            idx += 1
        
        nums2 = []
        for i in range(n):
            nums2.append(int(input[idx]))
            idx += 1
        
        result = find_kth_sorted_arrays(nums1, nums2, k)
        results.append(f"Case #{case_num}: {result}")
    
    return results