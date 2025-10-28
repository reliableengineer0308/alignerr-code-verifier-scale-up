def max_area(height):
    """
    Finds the maximum area between two lines that can hold water.
    Time: O(n), Space: O(1)
    """
    if not height or len(height) < 2:
        return 0

    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate current area
        current_height = min(height[left], height[right])
        width = right - left
        area = current_height * width

        # Update max area
        max_area = max(max_area, area)

        # Move the pointer at the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
