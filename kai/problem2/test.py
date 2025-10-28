#!/usr/bin/env python3
"""
Test file for Task Scheduling with Minimum Resources problem
"""

from solution import solve

def run_test(test_name, input_data, expected_output):
    """
    Run a single test case
    """
    try:
        result = solve(input_data)
        if result == expected_output:
            print(f"✓ {test_name}: PASSED")
            return True
        else:
            print(f"✗ {test_name}: FAILED")
            print(f"  Expected: {expected_output}, Got: {result}")
            print(f"  Input: {input_data}")
            return False
    except Exception as e:
        print(f"✗ {test_name}: FAILED with exception: {e}")
        return False

def main():
    """
    Main test function
    """
    test_cases = [
        # (test_name, input_list, expected_output)
        
        # Example from problem
        ("Example 1", [4, 1, 3, 2, 5, 4, 2, 6, 4], 2),
        
        # Single task
        ("Single task", [1, 1, 5], 1),
        
        # Two non-overlapping tasks
        ("Two non-overlapping", [2, 1, 2, 4, 3], 1),
        
        # Two overlapping tasks
        ("Two overlapping", [2, 1, 5, 2, 3], 2),
        
        # Three tasks, two overlapping
        ("Three tasks, two overlapping", [3, 1, 3, 2, 2, 5, 1], 2),
        
        # Many tasks that require 3 resources
        ("Three resources", [5, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6], 3),
        
        # Tasks that start and end at same time
        ("Same start and end", [3, 1, 2, 1, 3, 1, 4], 3),
        
        # Empty input
        ("Empty input", [], 0),
        
        # Large numbers
        ("Large numbers", [2, 1000000, 500000, 1500000, 300000], 1),
        
        # All tasks at same time
        ("All same start", [3, 1, 5, 1, 3, 1, 4], 3),
        
        # Chain of tasks
        ("Chain tasks", [3, 1, 2, 3, 2, 5, 1], 1),
    ]
    
    passed = 0
    total = len(test_cases)
    
    print("Running tests for Task Scheduling Problem:\n")
    
    for test_name, input_data, expected in test_cases:
        if run_test(test_name, input_data, expected):
            passed += 1
    
    print(f"\n{passed}/{total} tests passed.")
    
    if passed == total:
        print("🎉 All tests passed! ✓")
    else:
        print("❌ Some tests failed! ✗")

if __name__ == "__main__":
    main()