from typing import List, Dict

def schedule_tasks(tasks: List[Dict], capacity: int) -> int:
    """
    Schedule tasks to maximize profit under resource and deadline constraints.
    
    Returns maximum achievable profit.
    """
    n = len(tasks)
    if n == 0:
        return 0

    # Sort tasks by deadline for pruning
    sorted_tasks = sorted(tasks, key=lambda x: x["deadline"])
    
    max_time = max(t["deadline"] for t in tasks)
    
    # DP: dp[mask] = maximum profit achievable with tasks in mask
    dp = {0: 0}  # mask 0 → 0 profit
    best = 0
    
    for mask in range(1 << n):
        if mask not in dp:
            continue
        
        current_profit = dp[mask]
        best = max(best, current_profit)
        
        for i in range(n):
            if mask & (1 << i):
                continue  # Task i already scheduled
            
            task = sorted_tasks[i]
            # Try to schedule task i after all currently scheduled tasks
            # Find earliest start time
            last_end = 0
            for j in range(n):
                if mask & (1 << j):
                    prev_task = sorted_tasks[j]
                    last_end = max(last_end, prev_task["duration"])
            
            start_time = last_end
            end_time = start_time + task["duration"]
            
            # Check deadline and resource
            if end_time > task["deadline"]:
                continue
            # Resource check: task runs alone (no overlap)
            if task["resource"] > capacity:
                continue
                
            new_mask = mask | (1 << i)
            new_profit = current_profit + task["profit"]
            if new_mask not in dp or dp[new_mask] < new_profit:
                dp[new_mask] = new_profit
                best = max(best, new_profit)
    
    return best
