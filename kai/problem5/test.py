import solution

def run_test(test_name, input_data, expected_output):
    result = solution.solve(input_data)
    print(f"{test_name}: ", end="")
    if result == expected_output:
        print(f"PASSED (got {result})")
    else:
        print(f"FAILED (expected {expected_output}, got {result})")

def main():
    print("Running Network Packet Routing Tests...")
    print("=" * 50)
    
    # Test Case 1: Simple network
    # Router 0 (proc: 2) --5ms-- Router 1 (proc: 3) --4ms-- Router 2 (proc: 1)
    # S=0, D=2
    # Path: 0->1->2
    # Time = proc(0) + trans(0->1) + proc(1) + trans(1->2) = 2 + 5 + 3 + 4 = 14
    test1 = [3, 2, 0, 2, 2, 3, 1, 0, 1, 5, 1, 2, 4]
    run_test("Test 1 - Simple Path", test1, 14)
    
    # Test Case 2: Multiple paths
    # Router 0 (2) --3-- Router 1 (4) --2-- Router 3 (1)
    # Router 0 (2) --1-- Router 2 (1) --1-- Router 3 (1)
    # S=0, D=3
    # Path 1: 0->1->3 = 2 + 3 + 4 + 2 = 11
    # Path 2: 0->2->3 = 2 + 1 + 1 + 1 = 5
    test2 = [4, 4, 0, 3, 2, 4, 1, 1, 
             0, 1, 3, 
             0, 2, 1, 
             1, 3, 2, 
             2, 3, 1]
    run_test("Test 2 - Multiple Paths", test2, 5)
    
    # Test Case 3: Direct connection
    # Router 0 (1) --10-- Router 1 (1)
    # S=0, D=1
    # Time = proc(0) + trans(0->1) = 1 + 10 = 11 (no proc at destination)
    test3 = [2, 1, 0, 1, 1, 1, 0, 1, 10]
    run_test("Test 3 - Direct Connection", test3, 11)
    
    # Test Case 4: Unreachable destination
    test4 = [4, 2, 0, 3, 1, 2, 3, 4, 0, 1, 5, 1, 2, 3]
    run_test("Test 4 - Unreachable", test4, -1)
    
    # Test Case 5: Complex network
    # Processing: [3, 2, 4, 1, 5]
    # Edges: 0-1(2), 0-2(3), 1-2(1), 1-3(4), 2-3(2), 2-4(5), 3-4(1)
    # Best path: 0->1->3->4
    # Time = proc(0) + trans(0->1) + proc(1) + trans(1->3) + proc(3) + trans(3->4)
    #       = 3 + 2 + 2 + 4 + 1 + 1 = 13
    test5 = [5, 7, 0, 4, 3, 2, 4, 1, 5, 
             0, 1, 2, 
             0, 2, 3, 
             1, 2, 1, 
             1, 3, 4, 
             2, 3, 2, 
             2, 4, 5, 
             3, 4, 1]
    run_test("Test 5 - Complex Network", test5, 13)

if __name__ == "__main__":
    main()