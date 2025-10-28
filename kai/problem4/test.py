from solution import solve

def run_tests():
    """Run test cases with corrected expectations"""
    
    test_cases = [
        # (input, expected_output)
        # Format: [n, num1, num2, ...]
        
        # Classic example
        ([8, 10, 9, 2, 5, 3, 7, 101, 18], 4),
        
        # Single element
        ([1, 5], 1),
        
        # Empty array
        ([0], 0),
        
        # All decreasing
        ([5, 5, 4, 3, 2, 1], 1),
        
        # All increasing
        ([5, 1, 2, 3, 4, 5], 5),
        
        # All equal
        ([4, 7, 7, 7, 7], 1),
        
        # Complex case 1 - CORRECTED: LIS is actually 7: [-1, 0, 2, 3, 5, 7, 8]
        ([10, 3, 4, -1, 0, 6, 2, 3, 5, 7, 8], 7),
        
        # Complex case 2
        ([7, 2, 8, 1, 3, 4, 5, 6], 5),
        
        # Complex case 3
        ([9, 1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
        
        # Large numbers
        ([6, 100, 200, 300, 400, 500, 600], 6),
        
        # Negative numbers
        ([5, -5, -4, -3, -2, -1], 5),
        
        # Mixed positive and negative
        ([7, 10, -5, 0, 5, 2, 8, 1], 4),
        
        # Strictly increasing with duplicates in input
        ([6, 1, 2, 2, 3, 4, 5], 5),
        
        # Additional test case
        ([4, 1, 2, 3, 4], 4),
    ]
    
    print("Running Longest Increasing Subsequence tests...")
    print("=" * 60)
    
    all_passed = True
    for i, (input_data, expected) in enumerate(test_cases, 1):
        result = solve(input_data)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test {i}: {status}")
        
        # Show input details for failed tests
        if result != expected:
            all_passed = False
            n = input_data[0]
            nums = input_data[1:1+n]
            print(f"Input array: {nums}")
            print(f"Expected: {expected}, Got: {result}")
            print(f"*** MISMATCH ***")
        else:
            print(f"Expected: {expected}, Got: {result}")
        
        print("-" * 40)
    
    print("=" * 60)
    if all_passed:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed!")
    
    return all_passed

if __name__ == "__main__":
    run_tests()