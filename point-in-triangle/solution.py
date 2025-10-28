def is_point_in_triangle(p, v1, v2, v3):
    """
    Determines if point p is inside, on edge, or outside triangle (v1, v2, v3).
    Uses cross product method with epsilon for floating-point safety.
    Time: O(1), Space: O(1)
    """
    EPSILON = 1e-10

    def cross_product(o, a, b):
        """Cross product of vectors OA and OB"""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Compute cross products for each edge
    cp1 = cross_product(v1, v2, p)  # Edge v1->v2
    cp2 = cross_product(v2, v3, p)  # Edge v2->v3
    cp3 = cross_product(v3, v1, p)  # Edge v3->v1

    # Check if point is on any edge (cross product ~ 0)
    on_edge = (abs(cp1) < EPSILON or abs(cp2) < EPSILON or abs(cp3) < EPSILON)

    # Determine orientation of triangle (sign of area)
    triangle_area = cp1 + cp2 + cp3  # Sum of cross products ~ 2*area
    
    if on_edge:
        return "edge"

    # If all cross products have the same sign as the triangle area → inside
    if (cp1 >= -EPSILON and cp2 >= -EPSILON and cp3 >= -EPSILON) and triangle_area > EPSILON:
        return "inside"
    if (cp1 <= EPSILON and cp2 <= EPSILON and cp3 <= EPSILON) and triangle_area < -EPSILON:
        return "inside"

    return "outside"

