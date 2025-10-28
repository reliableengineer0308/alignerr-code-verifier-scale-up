def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merges overlapping intervals using sorting and linear scan.
    Time: O(n log n), Space: O(1) auxiliary (O(n) for output)
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]  # Initialize with first interval

    for current in intervals[1:]:
        last = merged[-1]
        # If current overlaps with last merged interval
        if current[0] <= last[1]:
            # Merge: extend the end of last interval
            last[1] = max(last[1], current[1])
        else:
            # No overlap: add current as new interval
            merged.append(current)

    return merged
