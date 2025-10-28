from solution import solve

def run_tests():
    """Run test cases and verify results"""
    
    test_cases = [
        # (input, expected_output)
        ([3, 2, 7, 10], 13),
        ([3, 2, 5, 10, 7], 15),
        ([5, 5, 10, 100, 10, 5], 110),
        ([1, 2, 3], 4),
        ([1, 20, 3], 20),
        ([], 0),
        ([5], 5),
        ([-1, -2, -3], 0),
        ([6, 7, 1, 3, 8, 2, 4], 19),
        ([4, 2, 3, 6, 5, 3], 13),  # Corrected from 12 to 13
        ([4, 2, 3, 6, 5, 3], 13),  # [4, 6, 3] = 13 is valid
        ([100, -1, 100, -1, 100], 300)
    ]
    
    print("Running tests...")
    print("=" * 50)
    
    all_passed = True
    for i, (input_data, expected) in enumerate(test_cases, 1):
        result = solve(input_data)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test {i}: {status}")
        print(f"Input: {input_data}")
        print(f"Expected: {expected}, Got: {result}")
        
        if result != expected:
            all_passed = False
            print(f"*** MISMATCH ***")
        print("-" * 30)
    
    print("=" * 50)
    if all_passed:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed!")
    
    return all_passed

if __name__ == "__main__":
    run_tests()