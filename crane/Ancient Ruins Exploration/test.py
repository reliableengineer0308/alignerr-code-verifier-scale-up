#!/usr/bin/env python3
import solution

def run_test(test_name, input_data, expected_output):
    """Run a single test case"""
    result = solution.solve(input_data)
    status = "PASS" if result == expected_output else "FAIL"
    print(f"{test_name}: {status}")
    print(f"  Input: {input_data}")
    print(f"  Expected: {expected_output}")
    print(f"  Got: {result}")
    print()
    return result == expected_output

def main():
    """Run all test cases"""
    print("Running Ancient Treasure Maze Tests")
    print("=" * 50)
    
    all_passed = True
    
    # Test Case 1: Basic test
    # Grid: 2x2, K=2
    # [1, 2]
    # [3, 4]
    # Valid paths: 
    # (0,0)→(0,1)→(1,1) = 1+2+4=7 (2 right moves)
    # (0,0)→(1,0)→(1,1) = 1+3+4=8 (2 down moves)
    # With K=2, both are valid. Maximum is 8.
    test1_input = [2, 2, 2, 1, 2, 3, 4]
    test1_expected = 8
    all_passed &= run_test("Test 1 - Basic", test1_input, test1_expected)
    
    # Test Case 2: Strict consecutive limit
    # Grid: 2x3, K=1
    # [1, 1, 1]
    # [1, 1, 1]
    # Must alternate directions. Valid paths:
    # (0,0)→(1,0)→(1,1)→(1,2) = 1+1+1+1=4
    # (0,0)→(0,1)→(1,1)→(1,2) = 1+1+1+1=4
    test2_input = [2, 3, 1, 1, 1, 1, 1, 1, 1]
    test2_expected = 4
    all_passed &= run_test("Test 2 - Strict Limit", test2_input, test2_expected)
    
    # Test Case 3: Impossible case
    # Grid: 1x4, K=1
    # [1, 1, 1, 1]
    # Need 3 right moves but K=1 → impossible
    test3_input = [1, 4, 1, 1, 1, 1, 1]
    test3_expected = -1
    all_passed &= run_test("Test 3 - Impossible", test3_input, test3_expected)
    
    # Test Case 4: Large values with optimal path
    # Grid: 3x3, K=2
    # [10, 1, 1]
    # [1, 100, 1]
    # [1, 1, 10]
    # Best path: (0,0)→(0,1)→(1,1)→(2,1)→(2,2) = 10+1+100+1+10=122
    # Or: (0,0)→(1,0)→(1,1)→(1,2)→(2,2) = 10+1+100+1+10=122
    test4_input = [3, 3, 2, 10, 1, 1, 1, 100, 1, 1, 1, 10]
    test4_expected = 122
    all_passed &= run_test("Test 4 - Optimal Path", test4_input, test4_expected)
    
    # Test Case 5: Single cell
    # Grid: 1x1, K=1
    # [5]
    test5_input = [1, 1, 1, 5]
    test5_expected = 5
    all_passed &= run_test("Test 5 - Single Cell", test5_input, test5_expected)
    
    # Test Case 6: Extreme values - horizontal impossible
    # Grid: 1x100, K=10
    # All values = 1000
    test6_input = [1, 100, 10] + [1000] * 100
    test6_expected = -1  # Impossible because need 99 right moves with K=10
    all_passed &= run_test("Test 6 - Extreme Horizontal", test6_input, test6_expected)
    
    # Test Case 7: Vertical extreme - impossible
    # Grid: 100x1, K=5
    # All values = 500
    test7_input = [100, 1, 5] + [500] * 100
    test7_expected = -1  # Impossible because need 99 down moves with K=5
    all_passed &= run_test("Test 7 - Extreme Vertical", test7_input, test7_expected)
    
    # Test Case 8: Zero coins
    # Grid: 2x2, K=2
    # [0, 0]
    # [0, 0]
    test8_input = [2, 2, 2, 0, 0, 0, 0]
    test8_expected = 0
    all_passed &= run_test("Test 8 - All Zeros", test8_input, test8_expected)
    
    # Test Case 9: Mixed path requirement
    # Grid: 4x4, K=3
    # [1, 1, 1, 1]
    # [1, 1, 1, 1]
    # [1, 1, 1, 1]
    # [1, 1, 1, 1]
    # Need 3 right + 3 down moves = 7 total moves collecting 7 coins
    test9_input = [4, 4, 3] + [1] * 16
    test9_expected = 7
    all_passed &= run_test("Test 9 - Mixed Path", test9_input, test9_expected)
    
    # Test Case 10: Large K with small grid
    # Grid: 3x3, K=10
    # [9, 1, 2]
    # [1, 8, 1]
    # [3, 1, 7]
    # Best path: (0,0)→(0,1)→(1,1)→(2,1)→(2,2) = 9+1+8+1+7=26
    # Or: (0,0)→(1,0)→(1,1)→(1,2)→(2,2) = 9+1+8+1+7=26
    test10_input = [3, 3, 10, 9, 1, 2, 1, 8, 1, 3, 1, 7]
    test10_expected = 26
    all_passed &= run_test("Test 10 - Large K", test10_input, test10_expected)

    # Test Case 11: Critical test - exactly at K limit
    # Grid: 1x3, K=2
    # [5, 5, 5]
    # Can do 2 right moves: 5+5+5=15
    test11_input = [1, 3, 2, 5, 5, 5]
    test11_expected = 15
    all_passed &= run_test("Test 11 - Exactly K Limit", test11_input, test11_expected)

    # Test Case 12: Critical test - exceeding K limit
    # Grid: 1x4, K=2  
    # [5, 5, 5, 5]
    # Need 3 right moves but K=2 → impossible
    test12_input = [1, 4, 2, 5, 5, 5, 5]
    test12_expected = -1
    all_passed &= run_test("Test 12 - Exceeding K Limit", test12_input, test12_expected)

    print("=" * 50)
    if all_passed:
        print("🎉 All tests PASSED!")
    else:
        print("❌ Some tests FAILED!")
    
    return all_passed

if __name__ == "__main__":
    main()