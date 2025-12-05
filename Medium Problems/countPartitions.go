func countPartitions(nums []int) int {
    is_odd := 0
    for _, n := range nums {
        is_odd ^= n % 2
    }
    if is_odd == 1 { return 0 } else { return len(nums) - 1 }
}
