// You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

// Return the total number of ways to partition nums under this condition.

// Since the answer may be too large, return it modulo 109 + 7.
import (
    "fmt"
    "container/list"
)
func countPartitions(nums []int, k int) int {
	const mod = 1_000_000_007
    n := len(nums)
    dp := make([]int, n+1)
    dp[0] = 1  
    
    prefix := make([]int, n+2)
    prefix[1] = 1  
	
	minQ := list.New()
	maxQ := list.New()
	var lag int
	for i, n := range nums{
		//keep em monotonic
		for minQ.Len() > 0 && nums[minQ.Front().Value.(int)]>= n{
			minQ.Remove(minQ.Front())
		}
		minQ.PushFront(i)
		for maxQ.Len() > 0 && nums[maxQ.Front().Value.(int)] <= n{
			maxQ.Remove(maxQ.Front())
		}
		maxQ.PushFront(i)
		//move lag
		for nums[maxQ.Back().Value.(int)] - nums[minQ.Back().Value.(int)] > k{
			lag++
            // fmt.Println( nums[maxQ[len(maxQ)-1]], nums[minQ[len(minQ)-1]])
			for maxQ.Back().Value.(int) < lag{
				maxQ.Remove(maxQ.Back())
			}
			for minQ.Back().Value.(int) < lag{
				minQ.Remove(minQ.Back())
			}
		}
		dp[i + 1] = (prefix[i + 1] - prefix[lag] + mod) % mod
		prefix[i + 2] = (prefix[i+1] + dp[i + 1] ) % mod
	}
	return dp[n]
}
