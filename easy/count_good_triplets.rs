impl Solution {
    pub fn count_good_triplets(arr: Vec<i32>, a: i32, b: i32, c: i32) -> i32 {
        let mut ans: i32 = 0;
        for i in 0..arr.len(){
            for j in i+1..arr.len(){
                for k in j+1..arr.len(){
                    if ((arr[i] - arr[j]).abs() <= a) && ((arr[j]-arr[k]).abs()<=b) && ((arr[k]-arr[i]).abs()<=c){
                        ans+=1
                    }
                }
            }
        }ans
    }
}
// Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

// A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

// 0 <= i < j < k < arr.length
// |arr[i] - arr[j]| <= a
// |arr[j] - arr[k]| <= b
// |arr[i] - arr[k]| <= c
// Where |x| denotes the absolute value of x.

// Return the number of good triplets.
