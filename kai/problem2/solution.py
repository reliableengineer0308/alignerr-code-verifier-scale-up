def solve(data):
    """
    Find minimum resources needed for tasks without overlapping
    
    Args:
        data: list of integers where:
            data[0] = number of tasks (n)
            data[1:2n+1] = pairs of (start_time, duration)
    
    Returns:
        int: minimum number of resources required
    """
    if not data:
        return 0
    
    n = data[0]
    tasks = []
    
    # Parse tasks from input data
    for i in range(n):
        start_idx = 1 + i * 2
        start = data[start_idx]
        duration = data[start_idx + 1]
        tasks.append((start, duration))
    
    # Create list of events: (time, type)
    # type: 1 for start, -1 for end
    events = []
    for start, duration in tasks:
        end = start + duration
        events.append((start, 1))   # start event
        events.append((end, -1))    # end event
    
    # Sort events: by time, end events before start events if same time
    events.sort(key=lambda x: (x[0], x[1]))
    
    current_resources = 0
    max_resources = 0
    
    for event in events:
        time, event_type = event
        current_resources += event_type
        max_resources = max(max_resources, current_resources)
    
    return max_resources