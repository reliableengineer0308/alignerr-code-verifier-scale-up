from typing import List, Optional

def max_constrained_subarray(arr: List[int], k: int, threshold: int) -> Optional[float]:
    """
    Finds the maximum product of a contiguous subarray of length k with at least one element >= threshold.
    
    Time: O(n), Space: O(1)
    Handles zeros, negatives, and edge cases.
    
    Args:
        arr: List of integers (1 <= len(arr) <= 10^5)
        k: Subarray length (1 <= k <= len(arr))
        threshold: Minimum value required in subarray
    
    Returns:
        Maximum product as float, or None if no valid subarray exists
    """
    n = len(arr)
    
    # Edge case: k exceeds array length
    if k > n:
        return None
    
    # Early exit: no element meets threshold
    if not any(x >= threshold for x in arr):
        return None

    max_product = None  # Best product found so far
    current_product = 1
    negative_count = 0
    zero_count = 0

    # Initialize first window [0, k-1]
    for i in range(k):
        val = arr[i]
        if val == 0:
            zero_count += 1
        elif val < 0:
            negative_count += 1
            current_product *= val
        else:
            current_product *= val  # val > 0

    # Check if first window is valid
    valid_in_window = any(arr[i] >= threshold for i in range(k))

    if valid_in_window:
        if zero_count > 0:
            candidate = 0.0
        else:
            candidate = abs(current_product) if (negative_count % 2 == 0) else -abs(current_product)
        max_product = candidate

    # Slide window: remove left, add right
    for right in range(k, n):
        left = right - k
        left_val = arr[left]
        right_val = arr[right]

        # Remove leftmost element
        if left_val == 0:
            zero_count -= 1
        elif left_val < 0:
            negative_count -= 1
            current_product //= left_val
        else:
            current_product //= left_val

        # Add rightmost element
        if right_val == 0:
            zero_count += 1
        elif right_val < 0:
            negative_count += 1
            current_product *= right_val
        else:
            current_product *= right_val

        # Recheck threshold condition for current window [left+1, right]
        window_start = left + 1
        window_end = right
        valid_in_window = any(
            arr[i] >= threshold 
            for i in range(window_start, window_end + 1)
        )

        # Evaluate current window if valid
        if valid_in_window:
            if zero_count > 0:
                candidate = 0.0
            else:
                candidate = (
                    abs(current_product) 
                    if (negative_count % 2 == 0)
                    else -abs(current_product)
                )
            if max_product is None or candidate > max_product:
                max_product = candidate

    return max_product
