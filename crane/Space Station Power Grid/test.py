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
    print("Running Space Station Power Grid Tests")
    print("=" * 50)
    
    all_passed = True
    
    # Test Case 1: Basic test
    test1_input = [4, 1, 2, 3, 1]
    test1_expected = 4
    all_passed &= run_test("Test 1 - Basic", test1_input, test1_expected)
    
    # Test Case 2: All positive
    test2_input = [3, 2, 3, 2]
    test2_expected = 3
    all_passed &= run_test("Test 2 - Circular Constraint", test2_input, test2_expected)
    
    # Test Case 3: Single node
    test3_input = [1, 100]
    test3_expected = 100
    all_passed &= run_test("Test 3 - Single Node", test3_input, test3_expected)
    
    # Test Case 4: Two nodes
    test4_input = [2, 5, 10]
    test4_expected = 10
    all_passed &= run_test("Test 4 - Two Nodes", test4_input, test4_expected)
    
    # Test Case 5: All zeros
    test5_input = [5, 0, 0, 0, 0, 0]
    test5_expected = 0
    all_passed &= run_test("Test 5 - All Zeros", test5_input, test5_expected)
    
    # Test Case 6: Large values with gaps
    test6_input = [5, 1000, 1, 1000, 1, 1000]
    test6_expected = 2000
    all_passed &= run_test("Test 6 - Large Values", test6_input, test6_expected)
    
    # Test Case 7: Extreme case - alternating high/low
    test7_input = [7, 10, 1, 10, 1, 10, 1, 10]
    test7_expected = 30
    all_passed &= run_test("Test 7 - Alternating Pattern", test7_input, test7_expected)
    
    # Test Case 8: All same values
    test8_input = [5, 5, 5, 5, 5, 5]
    test8_expected = 10
    all_passed &= run_test("Test 8 - All Same", test8_input, test8_expected)
    
    # Test Case 9: Large input size (performance test)
    large_input = [1000]
    for i in range(1000):
        if i % 2 == 0:
            large_input.append(1)
        else:
            large_input.append(100)
    test9_expected = 50000
    all_passed &= run_test("Test 9 - Large Input", large_input, test9_expected)
    
    # Test Case 10: Decreasing sequence
    test10_input = [6, 6, 5, 4, 3, 2, 1]
    test10_expected = 12
    all_passed &= run_test("Test 10 - Decreasing", test10_input, test10_expected)
    
    # Test Case 11: Edge case - three nodes with middle being largest
    test11_input = [3, 1, 100, 1]
    test11_expected = 100
    all_passed &= run_test("Test 11 - Middle Dominant", test11_input, test11_expected)
    
    # Test Case 12: Critical circular case - CORRECTED EXPECTATION
    # [3, 10, 3, 10, 3] - In linear arrays [3,10,3,10] and [10,3,10,3],
    # we CAN take both 10s since they are not adjacent
    test12_input = [5, 3, 10, 3, 10, 3]
    test12_expected = 20
    all_passed &= run_test("Test 12 - Circular Critical", test12_input, test12_expected)
    
    # Test Case 13: Another circular validation - CORRECTED EXPECTATION
    # [10, 1, 1, 10] - In linear arrays [10,1,1] and [1,1,10],
    # we can take 10+1=11 in both cases
    test13_input = [4, 10, 1, 1, 10]
    test13_expected = 11
    all_passed &= run_test("Test 13 - Circular Validation", test13_input, test13_expected)
    
    # Test Case 14: Even number of nodes
    test14_input = [6, 1, 2, 3, 4, 5, 6]
    test14_expected = 12
    all_passed &= run_test("Test 14 - Even Nodes", test14_input, test14_expected)

    print("=" * 50)
    if all_passed:
        print("🎉 All tests PASSED!")
    else:
        print("❌ Some tests FAILED!")
    
    return all_passed

if __name__ == "__main__":
    main()