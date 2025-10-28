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

# Test Case 1: Entire string is periodic
test1 = """6
1 2 1 2 1 2"""
run_test("Test 1", test1, "6")

# Test Case 2: Prefix of length 4 is periodic
test2 = """5
1 2 1 2 1"""
run_test("Test 2", test2, "4")

# Test Case 3: No periodic prefix
test3 = """3
1 2 3"""
run_test("Test 3", test3, "0")

# Test Case 4: All same elements
test4 = """4
5 5 5 5"""
run_test("Test 4", test4, "4")

# Test Case 5: Two element periodic
test5 = """2
7 7"""
run_test("Test 5", test5, "2")

# Test Case 6: Complex periodic pattern
test6 = """8
1 2 3 1 2 3 1 2"""
run_test("Test 6", test6, "6")

# Test Case 7: Multiple possible periods, take longest
test7 = """9
1 1 1 1 1 1 1 1 1"""
run_test("Test 7", test7, "9")

# Test Case 8: No periodicity at all
test8 = """4
1 2 3 4"""
run_test("Test 8", test8, "0")

print("All tests completed!")