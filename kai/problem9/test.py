from solution import solve

def run_test(test_num, input_data, expected):
    result = solve(input_data)
    print(f"Test {test_num}: {'PASS' if result == expected else 'FAIL'}")
    print(f"  Input: {input_data}")
    print(f"  Expected: {expected}, Got: {result}")
    print()

def main():
    # Test Case 1: Simple case with 2 buildings, 1 route
    # Building 0: 10 people, Building 1: safe zone
    # Route: 0->1, capacity 2 per hour = 12 in 6 hours
    # But only 10 people available
    test1 = [2, 1, 1,  # n=2, m=1, k=1
             1,         # safe zone at building 1
             10, 0,     # people in buildings
             0, 1, 2]   # route 0->1, capacity 2
    run_test(1, test1, 10)
    
    # Test Case 2: Limited by route capacity
    # Building 0: 20 people, Building 1: safe zone  
    # Route: 0->1, capacity 2 per hour = 12 in 6 hours
    test2 = [2, 1, 1,
             1,
             20, 0,
             0, 1, 2]
    run_test(2, test2, 12)
    
    # Test Case 3: Multiple paths
    # Building 0: 20 people, Building 1,2: safe zones
    # Routes: 0->1 (cap 1), 0->2 (cap 2)
    # Total capacity: (1+2)*6 = 18 per 6 hours
    test3 = [3, 2, 2,
             1, 2,
             20, 0, 0,
             0, 1, 1,
             0, 2, 2]
    run_test(3, test3, 18)
    
    # Test Case 4: Complex network
    # 4 buildings: 0(15 people), 1(10 people), 2(safe), 3(safe)
    # Routes: 0->1(cap3), 0->2(cap4), 1->3(cap2), 0->3(cap1)
    test4 = [4, 4, 2,
             2, 3,
             15, 10, 0, 0,
             0, 1, 3,
             0, 2, 4, 
             1, 3, 2,
             0, 3, 1]
    run_test(4, test4, 25)  # All 25 people can be evacuated
    
    # Test Case 5: Bottleneck situation
    # 0(20) -> 1 -> 2(safe), with limited middle capacity
    test5 = [3, 2, 1,
             2,
             20, 0, 0,
             0, 1, 3,  # 3 per hour
             1, 2, 2]  # 2 per hour - bottleneck!
    run_test(5, test5, 12)  # Limited by 2 per hour * 6 = 12

if __name__ == "__main__":
    main()