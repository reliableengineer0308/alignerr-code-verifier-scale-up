def trap(height):
    """
    Calculate total rain water trapped using two-pointer technique.
    Time: O(n), Space: O(1)
    """
    if not height or len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max = right_max = 0
    total_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]
            right -= 1

    return total_water
