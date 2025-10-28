import solution

def run_test(test_name, input_data, expected_output):
    result = solution.solve(input_data)
    status = "PASS" if result == expected_output else "FAIL"
    print(f"{test_name}: {status}")
    print(f"  Input: {input_data}")
    print(f"  Expected: {expected_output}")
    print(f"  Got: {result}")
    print()

def main():
    print("Running Treasure Hunter's Dilemma Tests\n")
    
    # Test Case 1: Basic case
    run_test("Test 1 - Basic", [5, 2, 7, 9, 3, 1], 12)
    
    # Test Case 2: All chambers have same gold
    run_test("Test 2 - Same values", [4, 5, 5, 5, 5], 10)
    
    # Test Case 3: Single chamber
    run_test("Test 3 - Single chamber", [1, 10], 10)
    
    # Test Case 4: Two chambers
    run_test("Test 4 - Two chambers", [2, 3, 4], 4)
    
    # Test Case 5: Empty chambers
    run_test("Test 5 - Empty", [0], 0)
    
    # Test Case 6: Large values with pattern
    run_test("Test 6 - Large pattern", [6, 1, 2, 3, 1, 4, 5], 13)
    
    # Test Case 7: All zeros
    run_test("Test 7 - All zeros", [5, 0, 0, 0, 0, 0], 0)
    
    # Test Case 8: Alternating high values
    run_test("Test 8 - Alternating", [6, 10, 1, 10, 1, 10, 1], 30)
    
    # Test Case 9: Increasing sequence
    run_test("Test 9 - Increasing", [5, 1, 2, 3, 4, 5], 9)
    
    # Test Case 10: Extreme case - maximum constraints
    run_test("Test 10 - Large input", [3, 10000, 10000, 10000], 20000)

if __name__ == "__main__":
    main()