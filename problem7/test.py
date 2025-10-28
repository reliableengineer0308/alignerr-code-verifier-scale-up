from solution import solve

def run_test(test_name, input_data, expected_output):
    print(f"Running {test_name}...")
    result = solve(input_data)
    print(f"Expected: {expected_output}")
    print(f"Got: {result}")
    
    if result == expected_output:
        print("✓ PASS")
    else:
        print("✗ FAIL")
    print()

# Test Case 1: Basic example from problem description
test1 = """20
3
1 2 3 1 2 1 2 3 1 2 3 4 1 2 3 5 6 7 8 9
1 2 3"""
run_test("Test 1", test1, "4")

# Test Case 2: Single character pattern
test2 = """10
1
1 1 1 1 1 2 1 1 1 1
1"""
run_test("Test 2", test2, "9")

# Test Case 3: No occurrences
test3 = """8
2
1 2 3 4 5 6 7 8
9 10"""
run_test("Test 3", test3, "0")

# Test Case 4: Overlapping occurrences
test4 = """10
2
1 1 1 1 1 1 1 1 1 1
1 1"""
run_test("Test 4", test4, "9")

# Test Case 5: Pattern equals text
test5 = """5
5
10 20 30 40 50
10 20 30 40 50"""
run_test("Test 5", test5, "1")

# Test Case 6: Multiple non-overlapping occurrences
test6 = """15
3
1 2 3 4 5 1 2 3 6 7 1 2 3 8 9
1 2 3"""
run_test("Test 6", test6, "3")

# Test Case 7: Pattern at beginning and end
test7 = """12
4
5 10 15 20 1 2 3 4 5 10 15 20
5 10 15 20"""
run_test("Test 7", test7, "2")

# Test Case 8: Complex overlapping case
test8 = """10
3
1 1 1 1 1 1 1 1 1 1
1 1 1"""
run_test("Test 8", test8, "8")

print("All tests completed!")