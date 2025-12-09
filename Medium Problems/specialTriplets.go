// You are given an integer array nums.

// A special triplet is defined as a triplet of indices (i, j, k) such that:

// 0 <= i < j < k < n, where n = nums.length
// nums[i] == nums[j] * 2
// nums[k] == nums[j] * 2
// Return the total number of special triplets in the array.

// Since the answer may be large, return it modulo 109 + 7.
import "fmt"
func specialTriplets(nums []int) int {
    left_map := make(map[int]int)
    right_map := make(map[int]int)
    leng := len(nums)
    toleft := make([]int, leng)
    toright := make([]int, leng)
    
    ans := 0
    for i, n := range nums{
        toleft[i] = left_map[n<<1]
        left_map[n]++
        n2 := nums[leng-i-1]
        toright[leng-i-1] = right_map[n2<<1]
        right_map[n2]++
    }
    // fmt.Println(toleft)
    for i := range nums{
        ans += toleft[i] * toright[i]
        ans = ans % 1_000_000_007
    }
    return ans
}
