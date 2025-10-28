from solution import schedule_tasks

def test_example_1():
    """Both tasks can run sequentially within capacity and deadlines."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 4, "resource": 3, "profit": 50},
        {"id": 2, "duration": 3, "deadline": 6, "resource": 2, "profit": 60}
    ]
    capacity = 5
    assert schedule_tasks(tasks, capacity) == 110

def test_example_2():
    """Cannot run both due to resource conflict; pick higher-profit task."""
    tasks = [
        {"id": 1, "duration": 4, "deadline": 5, "resource": 4, "profit": 100},
        {"id": 2, "duration": 3, "deadline": 7, "resource": 3, "profit": 80}
    ]
    capacity = 6  # 4+3=7 > 6 → conflict
    assert schedule_tasks(tasks, capacity) == 100

def test_single_task():
    """Only one task available; must accept if feasible."""
    tasks = [{"id": 1, "duration": 1, "deadline": 1, "resource": 1, "profit": 10}]
    assert schedule_tasks(tasks, 1) == 10


def test_impossible_task():
    """Task cannot meet its deadline regardless of resources."""
    tasks = [{"id": 1, "duration": 5, "deadline": 3, "resource": 1, "profit": 100}]
    assert schedule_tasks(tasks, 10) == 0

def test_resource_overflow():
    """Two tasks exceed capacity even if deadlines allow; pick best single."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 5, "resource": 6, "profit": 50},
        {"id": 2, "duration": 2, "deadline": 5, "resource": 5, "profit": 40}
    ]
    capacity = 10  # 6+5=11 > 10 → cannot run both
    result = schedule_tasks(tasks, capacity)
    assert result <= 50 and result >= 40  # Max of single tasks

def test_overlapping_deadlines():
    """Three tasks with tight deadlines; sequential scheduling required."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 3, "resource": 2, "profit": 30},
        {"id": 2, "duration": 2, "deadline": 4, "resource": 3, "profit": 40},
        {"id": 3, "duration": 1, "deadline": 2, "resource": 1, "profit": 20}
    ]
    capacity = 5
    # Schedule: t=0-1 (task3), t=1-3 (task1), t=3-5 (task2) → all meet deadlines
    assert schedule_tasks(tasks, capacity) == 90

def test_resource_conflict():
    """Tasks conflict on resource; pick higher-profit one."""
    tasks = [
        {"id": 1, "duration": 3, "deadline": 5, "resource": 4, "profit": 50},
        {"id": 2, "duration": 2, "deadline": 4, "resource": 4, "profit": 60}
    ]
    capacity = 7  # 4+4=8 > 7 → conflict
    assert schedule_tasks(tasks, capacity) == 60  # Task 2 has higher profit


def test_no_valid_schedule():
    """No task can be scheduled due to individual resource exceeds."""
    tasks = [
        {"id": 1, "duration": 5, "deadline": 5, "resource": 10, "profit": 100},
        {"id": 2, "duration": 4, "deadline": 4, "resource": 8, "profit": 80}
    ]
    capacity = 9  # Both exceed capacity individually
    assert schedule_tasks(tasks, capacity) == 0


def test_identical_tasks():
    """Two identical tasks; both can run sequentially."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 4, "resource": 2, "profit": 25},
        {"id": 2, "duration": 2, "deadline": 4, "resource": 2, "profit": 25}
    ]
    capacity = 4  # 2+2=4 ≤ capacity
    assert schedule_tasks(tasks, capacity) == 50

def test_tight_deadlines():
    """Tasks with consecutive deadlines; must schedule in order."""
    tasks = [
        {"id": 1, "duration": 1, "deadline": 1, "resource": 1, "profit": 10},
        {"id": 2, "duration": 1, "deadline": 2, "resource": 1, "profit": 15},
        {"id": 3, "duration": 1, "deadline": 3, "resource": 1, "profit": 20}
    ]
    capacity = 1  # Must run sequentially
    # Schedule: t=0→1 (task1), t=1→2 (task2), t=2→3 (task3)
    assert schedule_tasks(tasks, capacity) == 45


def test_high_profit_low_duration():
    """Short high-profit task should be prioritized."""
    tasks = [
        {"id": 1, "duration": 5, "deadline": 10, "resource": 5, "profit": 100},
        {"id": 2, "duration": 1, "deadline": 2, "resource": 1, "profit": 90}
    ]
    capacity = 6  # Can fit both: task2 first, then task1
    assert schedule_tasks(tasks, capacity) == 190


def test_partial_overlap_allowed():
    """Tasks could overlap but deadlines force sequential execution."""
    tasks = [
        {"id": 1, "duration": 3, "deadline": 6, "resource": 2, "profit": 40},
        {"id": 2, "duration": 2, "deadline": 5, "resource": 3, "profit": 50}
    ]
    capacity = 5  # 2+3=5 ≤ capacity → could run in parallel
    # But deadlines: task2 must finish by t=5, task1 by t=6
    # Optimal: task2 at t=0-2, task1 at t=2-5 → total profit 90
    assert schedule_tasks(tasks, capacity) == 90


def test_large_profit_gap():
    """Dramatic profit difference; pick high-value short task."""
    tasks = [
        {"id": 1, "duration": 10, "deadline": 20, "resource": 1, "profit": 10},
        {"id": 2, "duration": 1, "deadline": 2, "resource": 1, "profit": 200}
    ]
    capacity = 2  # Prioritize task2 (200 > 10)
    assert schedule_tasks(tasks, capacity) == 200

def test_edge_case_zero_profit():
    """Zero-profit task should not affect result."""
    tasks = [{"id": 1, "duration": 1, "deadline": 1, "resource": 1, "profit": 0}]
    capacity = 1
    assert schedule_tasks(tasks, capacity) == 0

def test_empty_task_list():
    """No tasks provided."""
    assert schedule_tasks([], 5) == 0

def test_all_tasks_exceed_capacity():
    """All tasks require more resources than available; no task can be scheduled."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 4, "resource": 6, "profit": 50},
        {"id": 2, "duration": 3, "deadline": 6, "resource": 7, "profit": 40}
    ]
    capacity = 5  # Both tasks exceed capacity individually
    assert schedule_tasks(tasks, capacity) == 0


def test_single_task_exceeds_capacity():
    """One task exceeds capacity; others are feasible."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 4, "resource": 6, "profit": 50},  # Exceeds
        {"id": 2, "duration": 2, "deadline": 5, "resource": 3, "profit": 40}   # Feasible
    ]
    capacity = 5
    assert schedule_tasks(tasks, capacity) == 40  # Only task 2 can run

def test_identical_deadlines():
    """Tasks with same deadline; schedule higher-profit first."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 5, "resource": 2, "profit": 30},
        {"id": 2, "duration": 2, "deadline": 5, "resource": 2, "profit": 40},
        {"id": 3, "duration": 1, "deadline": 5, "resource": 1, "profit": 20}
    ]
    capacity = 5  # Can fit all sequentially
    # Optimal: task2 (40) → task1 (30) → task3 (20) = 90
    assert schedule_tasks(tasks, capacity) == 90

def test_profit_density_priority():
    """Prioritize tasks with higher profit-per-resource ratio."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 4, "resource": 1, "profit": 50},  # 50/1 = 50
        {"id": 2, "duration": 3, "deadline": 6, "resource": 5, "profit": 80}   # 80/5 = 16
    ]
    capacity = 6  # Can run both sequentially
    assert schedule_tasks(tasks, capacity) == 130  # Both fit


def test_duration_vs_profit_tradeoff():
    """Choose between long high-profit vs short low-profit task."""
    tasks = [
        {"id": 1, "duration": 5, "deadline": 10, "resource": 3, "profit": 100},
        {"id": 2, "duration": 1, "deadline": 2, "resource": 1, "profit": 25}
    ]
    capacity = 4  # Can run both: task2 first, then task1
    assert schedule_tasks(tasks, capacity) == 125


def test_non_overlapping_windows():
    """Tasks have non-overlapping time windows; must pick best combination."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 3, "resource": 2, "profit": 30},  # t=0-2
        {"id": 2, "duration": 2, "deadline": 6, "resource": 3, "profit": 50},  # t=4-6
        {"id": 3, "duration": 1, "deadline": 2, "resource": 1, "profit": 20}   # t=1-2
    ]
    capacity = 5
    # Task1 and task3 conflict (overlap at t=1-2); task2 starts at t=4
    # Best: task3 (20) + task2 (50) = 70 (task1 excluded due to conflict)
    assert schedule_tasks(tasks, capacity) == 70


def test_resource_reuse_after_completion():
    """Resource is freed after task completes; allows subsequent tasks."""
    tasks = [
        {"id": 1, "duration": 2, "deadline": 4, "resource": 4, "profit": 60},
        {"id": 2, "duration": 2, "deadline": 6, "resource": 4, "profit": 50}
    ]
    capacity = 4  # Cannot run both simultaneously, but can run sequentially
    # Schedule: task1 (t=0-2) → task2 (t=2-4) → both meet deadlines
    assert schedule_tasks(tasks, capacity) == 110


def test_strict_sequential_dependency():
    """Tasks must be scheduled in strict order due to deadlines."""
    tasks = [
        {"id": 1, "duration": 1, "deadline": 1, "resource": 1, "profit": 10},
        {"id": 2, "duration": 1, "deadline": 2, "resource": 1, "profit": 20},
        {"id": 3, "duration": 1, "deadline": 3, "resource": 1, "profit": 30}
    ]
    capacity = 1  # Must run in order: 1→2→3
    assert schedule_tasks(tasks, capacity) == 60


def run_all_tests():
    tests = [
        test_example_1,
        test_example_2,
        test_single_task,
        test_impossible_task,
        test_resource_overflow,
        test_overlapping_deadlines,
        test_resource_conflict,
        test_no_valid_schedule,
        test_identical_tasks,
        test_tight_deadlines,
        test_high_profit_low_duration,
        test_partial_overlap_allowed,
        test_large_profit_gap,
        test_edge_case_zero_profit,
        test_empty_task_list,
        test_all_tasks_exceed_capacity,
        test_single_task_exceeds_capacity,
        test_identical_deadlines,
        test_profit_density_priority,
        test_duration_vs_profit_tradeoff,
        test_non_overlapping_windows,
        test_resource_reuse_after_completion,
        test_strict_sequential_dependency
    ]
    
    passed = 0
    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__} PASSED")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} FAILED: {e}")
        except Exception as e:
            print(f"⚠ {test.__name__} ERRORED: {e}")
    
    print(f"\nResults: {passed}/{len(tests)} tests passed")
    return 0 if passed == len(tests) else 1

if __name__ == "__main__":
    exit(run_all_tests())
