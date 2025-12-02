// You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

// A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

// Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

// Since the answer may be very large, return it modulo 109 + 7.
func countTrapezoids(points [][]int) int {
    // i will start by counting horizontal lines
    bars := make(map[int]int)
	// levels := 0
    const Mod = 1_000_000_007
	count := 0
    sum := 0
	for _, p := range points{
		bars[p[1]]++
	}
    for _, val := range bars{
        count += sum * val * (val - 1) / 2
        sum += val * (val - 1) / 2
        count   %=  Mod
        sum     %=  Mod
    }
	return count
}
