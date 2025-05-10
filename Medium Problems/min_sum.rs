impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let (mut sum1, mut z1, mut sum2, mut z2) = (0i64, 0i64, 0i64, 0i64);
        for n in nums1{
            sum1 += n as i64;
            if n == 0{z1 += 1;}
        }
        for n in nums2{
            sum2 += n as i64;
            if n == 0{z2 += 1;}
        }
        if sum1 < sum2 + z2 && z1 == 0 || sum2 < sum1 + z1 && z2 == 0{
            -1
        }else{
            (sum1 + z1).max(sum2 + z2)
        }
    }
}
// You are given two arrays nums1 and nums2 consisting of positive integers.

// You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

// Return the minimum equal sum you can obtain, or -1 if it is impossible.
