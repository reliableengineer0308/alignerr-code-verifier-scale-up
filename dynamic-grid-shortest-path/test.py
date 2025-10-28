from solution import shortest_path_dynamic


def test_example_1():
    """Basic case: avoid obstacle at t=1 by taking alternate path."""
    grid = [[0, 0], [0, 0]]
    start = (0, 0)
    end = (1, 1)
    obstacles = [(1, 1, 0)]  # (1,0) blocked at t=1
    assert shortest_path_dynamic(grid, start, end, obstacles) == 3


def test_example_2():
    """Impossible: destination blocked at arrival time."""
    grid = [[0, 1], [0, 0]]
    start = (0, 0)
    end = (1, 1)
    obstacles = [(2, 1, 1)]  # (1,1) blocked at t=2
    assert shortest_path_dynamic(grid, start, end, obstacles) == -1


def test_example_3():
    """Complex path avoiding two time-varying obstacles."""
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    start = (0, 0)
    end = (2, 2)
    obstacles = [(3, 2, 1), (4, 1, 2)]  # (2,1)@t=3, (1,2)@t=4
    assert shortest_path_dynamic(grid, start, end, obstacles) == 6


def test_immediate_obstacle():
    """Start cell becomes blocked at t=0 → impossible."""
    grid = [[0]]
    start = (0, 0)
    end = (0, 0)
    obstacles = [(0, 0, 0)]
    assert shortest_path_dynamic(grid, start, end, obstacles) == -1

def test_wait_strategy():
    """Must wait to avoid future obstacle."""
    grid = [[0, 0, 0]]
    start = (0, 0)
    end = (0, 2)
    obstacles = [(1, 0, 1)]  # Middle cell blocked at t=1
    # Path: wait at (0,0) for t=1, then move → total time=3
    assert shortest_path_dynamic(grid, start, end, obstacles) == 3

def test_no_obstacles():
    """Normal BFS with no time constraints."""
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start = (0, 0)
    end = (2, 2)
    obstacles = []
    assert shortest_path_dynamic(grid, start, end, obstacles) == 4  # Min steps


def test_permanent_block():
    """Permanently blocked cell must be avoided."""
    grid = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    start = (0, 0)
    end = (2, 2)
    obstacles = []  # Only permanent blocks exist
    assert shortest_path_dynamic(grid, start, end, obstacles) == 6


def test_edge_wait():
    """Waiting at destination is allowed but unnecessary."""
    grid = [[0, 0]]
    start = (0, 0)
    end = (0, 1)
    obstacles = [(1, 0, 1)]  # Destination blocked at t=1
    # Must arrive at t=0 or t≥2 → best is t=2 (wait then move)
    assert shortest_path_dynamic(grid, start, end, obstacles) == 2


def test_unreachable_due_to_cycle():
    """Obstacles create periodic blockade; path must find gap."""
    grid = [[0, 0, 0, 0]]
    start = (0, 0)
    end = (0, 3)
    # Cells (0,1) and (0,2) alternate blocking
    obstacles = [(1, 0, 1), (2, 0, 2), (3, 0, 1), (4, 0, 2)]
    # Optimal: wait t=0→1, move (0,0)→(0,1) at t=1 (blocked!), so wait t=1→2, then:
    # t=2: (0,0)→(0,1); t=3: (0,1)→(0,2); t=4: (0,2)→(0,3)
    assert shortest_path_dynamic(grid, start, end, obstacles) == 5


def test_large_grid():
    """Larger grid with sparse obstacles."""
    grid = [[0]*10 for _ in range(10)]
    start = (0, 0)
    end = (9, 9)
    obstacles = [(5, 5, 5), (6, 6, 6)]  # Localized blocks
    # Manhattan distance = 18; obstacles don't block optimal path
    assert shortest_path_dynamic(grid, start, end, obstacles) >= 18


def test_corner_cases():
    """Edge cases: same start/end, single cell."""
    # Case 1: start == end
    grid1 = [[0]]
    assert shortest_path_dynamic(grid1, (0,0), (0,0), []) == 0
    # Case 2: 1x2 grid
    grid2 = [[0, 0]]
    assert shortest_path_dynamic(grid2, (0,0), (0,1), []) == 1


def test_time_overflow():
    """Obstacles stop at t=100; after that, free movement."""
    grid = [[0, 0], [0, 0]]
    start = (0, 0)
    end = (1, 1)
    # Blocked until t=99, but free at t=100+
    obstacles = [(t, 1, 1) for t in range(100)]
    result = shortest_path_dynamic(grid, start, end, obstacles)
    assert result >= 102  # Wait until t=100, then 2 moves


def run_all_tests():
    tests = [
        test_example_1, test_example_2, test_example_3,
        test_immediate_obstacle, test_wait_strategy,
        test_no_obstacles, test_permanent_block,
        test_edge_wait, test_unreachable_due_to_cycle,
        test_large_grid, test_corner_cases, test_time_overflow
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
