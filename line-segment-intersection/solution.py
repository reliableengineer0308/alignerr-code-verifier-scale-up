def segments_intersect(a1, a2, b1, b2):
    """
    Determines if two line segments intersect using orientation tests and distance checks.
    
    Args:
        a1, a2: tuples (x, y) - endpoints of first segment
        b1, b2: tuples (x, y) - endpoints of second segment
    Returns:
        bool: True if segments intersect (including endpoints), False otherwise
    """
    EPSILON = 1e-10      # Floating-point tolerance
    MIN_DIST_SQ = 1e-6  # Minimum squared distance for "near miss! rejection

    def cross(o, a, b):
        """Compute 2D cross product of vectors OA and OB"""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def ccw(a, b, c):
        """Orientation test: >0 CCW, <0 CW, 0 collinear"""
        val = cross(a, b, c)
        if abs(val) < EPSILON:
            return 0
        return 1 if val > 0 else -1

    def point_distance_sq(p1, p2):
        """Squared distance between two points"""
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    def is_point_on_segment(p, a, b):
        """Check if point p lies on segment ab"""
        if ccw(a, b, p) != 0:  # Not collinear
            return False
        # Bounding box check with EPSILON tolerance
        return (min(a[0], b[0]) - EPSILON <= p[0] <= max(a[0], b[0]) + EPSILON and
                min(a[1], b[1]) - EPSILON <= p[1] <= max(a[1], b[1]) + EPSILON)

    def segments_bbox_overlap(s1, s2, t1, t2):
        """Quick bounding box overlap check"""
        return not (max(s1[0], s2[0]) < min(t1[0], t2[0]) or
                   max(t1[0], t2[0]) < min(s1[0], s2[0]) or
                   max(s1[1], s2[1]) < min(t1[1], t2[1]) or
                   max(t1[1], t2[1]) < min(s1[1], s2[1]))

    # Early rejection: bounding boxes don't overlap
    if not segments_bbox_overlap(a1, a2, b1, b2):
        return False

    # Orientation tests
    o1 = ccw(a1, a2, b1)
    o2 = ccw(a1, a2, b2)
    o3 = ccw(b1, b2, a1)
    o4 = ccw(b1, b2, a2)

    # General case: segments straddle each other
    if o1 != o2 and o3 != o4:
        return True

    # Special cases: endpoints on segments
    if (is_point_on_segment(b1, a1, a2) or
        is_point_on_segment(b2, a1, a2) or
        is_point_on_segment(a1, b1, b2) or
        is_point_on_segment(a2, b1, b2)):
        return True

    # Final check: reject near-miss cases using distance
    def min_dist_to_segment_sq(seg_start, seg_end, point):
        """Minimum squared distance from point to segment"""
        seg_vec_x = seg_end[0] - seg_start[0]
        seg_vec_y = seg_end[1] - seg_start[1]
        point_vec_x = point[0] - seg_start[0]
        point_vec_y = point[1] - seg_start[1]

        seg_len_sq = seg_vec_x**2 + seg_vec_y**2
        if seg_len_sq < EPSILON:  # Degenerate segment (point)
            return point_distance_sq(point, seg_start)


        t = (point_vec_x * seg_vec_x + point_vec_y * seg_vec_y) / seg_len_sq
        t = max(0.0, min(1.0, t))  # Clamp to segment
        proj_x = seg_start[0] + t * seg_vec_x
        proj_y = seg_start[1] + t * seg_vec_y
        return point_distance_sq(point, (proj_x, proj_y))


    min_dist_sq = min(
        min_dist_to_segment_sq(a1, a2, b1),
        min_dist_to_segment_sq(a1, a2, b2),
        min_dist_to_segment_sq(b1, b2, a1),
        min_dist_to_segment_sq(b1, b2, a2)
    )

    return min_dist_sq <= MIN_DIST_SQ
