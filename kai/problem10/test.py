from solution import solve

def run_test(test_num, input_data, expected):
    result = solve(input_data)
    print(f"Test {test_num}: {'PASS' if result == expected else 'FAIL'}")
    print(f"  Expected: {expected}, Got: {result}")
    if result != expected:
        print(f"  Input: {input_data}")
    print()

def main():
    # Test Case 1: Simple case - 1 restaurant, 1 customer, direct connection
    # Restaurant at location 0 with 10 drivers
    # Customer at location 1 with 8 demand  
    # Road 0->1 with capacity 15
    test1 = [
        2, 1, 1, 1,  # n=2, m=1, r=1, c=1
        0, 10,        # restaurant at 0 with 10 drivers
        1, 8,         # customer at 1 with 8 demand
        0, 1, 15      # road 0->1, capacity 15
    ]
    run_test(1, test1, 8)  # Limited by customer demand
    
    # Test Case 2: Multiple paths
    # Restaurant at 0 (15 drivers), Customers at 3 (10), 4 (8)
    # Roads: 0->1 (10), 0->2 (8), 1->3 (7), 2->3 (5), 1->4 (6), 2->4 (4)
    test2 = [
        5, 6, 1, 2,
        0, 15,
        3, 10, 4, 8,
        0, 1, 10,
        0, 2, 8,
        1, 3, 7,
        2, 3, 5, 
        1, 4, 6,
        2, 4, 4
    ]
    run_test(2, test2, 15)  # All 15 drivers can be utilized
    
    # Test Case 3: Complex network with bottlenecks
    # 2 restaurants, 2 customers
    # Restaurant 0: 12 drivers, Restaurant 1: 8 drivers
    # Customer 4: 15 demand, Customer 5: 10 demand
    # Roads with various capacities creating bottlenecks
    test3 = [
        6, 8, 2, 2,
        0, 12, 1, 8,
        4, 15, 5, 10,
        0, 2, 10,
        0, 3, 8,
        1, 2, 7,
        1, 3, 6,
        2, 4, 12,
        2, 5, 9,
        3, 4, 11,
        3, 5, 8
    ]
    run_test(3, test3, 20)  # Total available drivers = 20
    
    # Test Case 4: Limited by road capacities
    # Restaurant 0: 20 drivers, Customer 2: 20 demand
    # But middle road has limited capacity
    test4 = [
        3, 2, 1, 1,
        0, 20,
        2, 20,
        0, 1, 15,  # bottleneck
        1, 2, 15   # bottleneck
    ]
    run_test(4, test4, 15)  # Limited by road capacity
    
    # Test Case 5: Multiple restaurants to multiple customers
    # Restaurants: 0(10), 1(8); Customers: 4(12), 5(9)
    # Complex road network
    test5 = [
        6, 7, 2, 2,
        0, 10, 1, 8,
        4, 12, 5, 9,
        0, 2, 8,
        0, 3, 7,
        1, 2, 6,
        1, 3, 5,
        2, 4, 10,
        2, 5, 8,
        3, 4, 9
    ]
    run_test(5, test5, 18)  # Total drivers = 18

if __name__ == "__main__":
    main()