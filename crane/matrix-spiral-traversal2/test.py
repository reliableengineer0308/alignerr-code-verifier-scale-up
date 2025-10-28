from solution import spiral_order

def test_square_matrix():
    """Test spiral traversal on a 3x3 square matrix."""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

def test_rectangular_matrix():
    """Test spiral traversal on a 3x4 rectangular matrix."""
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert spiral_order(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

def test_single_row():
    """Test a single-row matrix (1xn)."""
    matrix = [[1, 2, 3, 4, 5]]
    assert spiral_order(matrix) == [1, 2, 3, 4, 5]

def test_single_column():
    """Test a single-column matrix (mx1)."""
    matrix = [
        [1],
        [2],
        [3],
        [4]
    ]
    assert spiral_order(matrix) == [1, 2, 3, 4]

def test_2x2_matrix():
    """Test a small 2x2 matrix."""
    matrix = [
        [1, 2],
        [3, 4]
    ]
    assert spiral_order(matrix) == [1, 2, 4, 3]

def test_1x1_matrix():
    """Test a 1x1 matrix (single element)."""
    matrix = [[42]]
    assert spiral_order(matrix) == [42]

def test_tall_matrix():
    """Test a tall matrix (4x2)."""
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
    assert spiral_order(matrix) == [1, 2, 4, 6, 8, 7, 5, 3]

def test_wide_matrix():
    """Test a wide matrix (2x3)."""
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert spiral_order(matrix) == [1, 2, 3, 6, 5, 4]

def test_empty_matrix():
    """Test an empty matrix (edge case)."""
    matrix = []
    assert spiral_order(matrix) == []

def test_matrix_with_zeros():
    """Test matrix containing zeros."""
    matrix = [
        [0, 0],
        [0, 0]
    ]
    assert spiral_order(matrix) == [0, 0, 0, 0]

def test_negative_numbers():
    """Test matrix with negative numbers."""
    matrix = [
        [-1, -2],
        [-3, -4]
    ]
    assert spiral_order(matrix) == [-1, -2, -4, -3]

def run_all_tests():
    """Run all test functions and report results."""
    test_functions = [
        test_square_matrix,
        test_rectangular_matrix,
        test_single_row,
        test_single_column,
        test_2x2_matrix,
        test_1x1_matrix,
        test_tall_matrix,
        test_wide_matrix,
        test_empty_matrix,
        test_matrix_with_zeros,
        test_negative_numbers
    ]

    passed = 0
    total = len(test_functions)

    print("Running spiral_order() tests...\n")

    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ PASSED: {test_func.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"✗ FAILED: {test_func.__name__} — Assertion error: {e}")
        except Exception as e:
            print(f"✗ ERROR: {test_func.__name__} — Unexpected error: {e}")

    print(f"\n=== RESULTS ===")
    print(f"{passed}/{total} tests passed")

    if passed == total:
        print("✓ All tests passed successfully!")
        return 0
    else:
        print(f"✗ {total - passed} tests failed.")
        return 1

if __name__ == "__main__":
    # Try to use pytest if available for detailed output
    try:
        import pytest
        pytest.main([__file__, "-v"])
    except ImportError:
        # Fall back to manual test runner
        print("pytest not found. Running tests manually...\n")
        exit(run_all_tests())
