from solution import min_cost_connect_points


def test_single_point():
    """n=1 → no edges needed."""
    assert min_cost_connect_points([[0, 0]], []) == 0


def test_two_points_allowed():
    """Two points, no forbidden edges → connect directly."""
    points = [[0, 0], [3, 4]]
    assert min_cost_connect_points(points, []) == 7  # |0-3| + |0-4| = 7


def test_two_points_forbidden():
    """Two points but the only edge is forbidden → impossible."""
    points = [[1, 1], [2, 2]]
    assert min_cost_connect_points(points, [(0, 1)]) == -1

def test_example_1():
    """From problem statement: 5 points, one forbidden edge."""
    points = [[0,0], [2,2], [3,10], [5,2], [7,0]]
    forbidden = [(1, 4)]  # Don't connect point 1 and 4
    result = min_cost_connect_points(points, forbidden)
    assert result == 20, f"Expected 20, got {result}"


def test_fully_forbidden_triangle():
    """3 points, all possible edges forbidden → impossible to connect."""
    points = [[3, 12], [-2, 5], [-4, 1]]
    forbidden = [(0,1), (1,2), (0,2)]
    assert min_cost_connect_points(points, forbidden) == -1


def test_square_with_one_forbidden():
    """4 points in a square, one diagonal forbidden. MST uses 3 edges of cost 1 each."""
    points = [[0,0], [0,1], [1,0], [1,1]]
    forbidden = [(0,3)]  # Forbid diagonal (0,3)
    # Valid MST: (0,1), (0,2), (1,3) → total cost = 1+1+1 = 3
    assert min_cost_connect_points(points, forbidden) == 3


def test_disconnected_by_forbidden():
    """4 points: A,B,C,D. Forbidden edges split graph into two components."""
    points = [[0,0], [1,0], [0,5], [1,5]]
    # Connect A-B and C-D, but forbid A-C, A-D, B-C, B-D → two separate edges, not connected
    forbidden = [(0,2), (0,3), (1,2), (1,3)]
    assert min_cost_connect_points(points, forbidden) == -1  # Can't connect all 4


def test_three_points_one_forbidden():
    """
    3 points: A(0,0), B(4,0), C(2,3)
    Forbidden: (A,B) → can't connect directly.
    Must form MST using A-C and B-C.
    
    Manhattan distances:
      - A to C: |0-2| + |0-3| = 2 + 3 = 5
      - B to C: |4-2| + |0-3| = 2 + 3 = 5
    Total MST cost = 5 + 5 = 10
    """
    points = [[0, 0], [4, 0], [2, 3]]
    forbidden = [(0, 1)]  # Forbid edge between point 0 (A) and point 1 (B)

    result = min_cost_connect_points(points, forbidden)
    
    assert result == 10, (
        f"Expected MST cost 10 (via A-C and B-C), but got {result}. "
        "Check if forbidden edge (0,1) was incorrectly used or graph is disconnected."
    )

def test_all_edges_allowed():
    """5 points, no forbidden edges → standard MST."""
    points = [[1,2], [3,4], [5,6], [7,8], [9,10]]
    result = min_cost_connect_points(points, [])
    # All Manhattan distances are even; MST will pick 4 cheapest edges
    # This tests general MST logic
    assert isinstance(result, int) and result > 0


def test_large_coordinates():
    """Points with large coordinates but small relative distances."""
    points = [[1000,1000], [1001,1000], [1000,1001], [1001,1001]]
    # 2x2 grid at (1000,1000) corner
    assert min_cost_connect_points(points, []) == 3  # MST cost: 1+1+1


def test_star_topology_forced():
    """One central point connected to all others; some edges forbidden but alternatives exist."""
    points = [[0,0], [1,0], [0,1], [-1,0], [0,-1]]
    # Center at (0,0), others at distance 1
    forbidden = [(0,1), (0,2)]  # Can't use center→right, center→up
    # Must route via other points → total cost increases
    result = min_cost_connect_points(points, forbidden)
    assert 5 <= result <= 8  # Lower bound: 4×1 (if direct possible), upper: detours


def test_impossible_due_to_isolation():
    """One point is isolated due to forbidden edges."""
    points = [[0,0], [10,10], [11,11], [12,12]]
    # Point 0 is far away; all edges from it are forbidden
    forbidden = [(0,1), (0,2), (0,3)]
    # Points 1,2,3 form a chain, but point 0 can't connect
    assert min_cost_connect_points(points, forbidden) == -1


def run_all_tests():
    tests = [
        test_single_point,
        test_two_points_allowed,
        test_two_points_forbidden,
        test_example_1,
        test_fully_forbidden_triangle,
        test_square_with_one_forbidden,
        test_disconnected_by_forbidden,
        test_three_points_one_forbidden,
        test_all_edges_allowed,
        test_large_coordinates,
        test_star_topology_forced,
        test_impossible_due_to_isolation
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
