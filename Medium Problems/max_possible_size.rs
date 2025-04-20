impl Solution {
    pub fn maximum_possible_size(nums: Vec<i32>) -> i32 {
        let (mut highest, mut count) = (0, 0);
        for num in nums.into_iter(){
            if num >= highest{
                highest = num;
                count+=1;
            }
        }count
    }
}
// You are given an integer array nums. In one operation, you can select a subarray and replace it with a single element equal to its maximum value.

// Return the maximum possible size of the array after performing zero or more operations such that the resulting array is non-decreasing.
