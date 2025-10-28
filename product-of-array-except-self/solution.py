def product_except_self(nums: list[int]) -> list[int]:
    """
    Returns an array where each element is the product of all other elements except self.
    
    Uses two-pass method:
    - First pass: store prefix product (product of all elements to the left)
    - Second pass: multiply by suffix product (product of all to the right)
    
    Time: O(n), Space: O(1) auxiliary (output array not counted)
    """
    n = len(nums)
    result = [1] * n  # Initialize with 1s

    # First pass: prefix products
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    # Second pass: suffix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]

    return result
