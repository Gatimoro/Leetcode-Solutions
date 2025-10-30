// You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.

// In one operation you can choose any subarray from initial and increment each value by one.

// Return the minimum number of operations to form a target array from initial.

// The test cases are generated so that the answer fits in a 32-bit integer.

impl Solution {
    pub fn min_number_operations(mut target: Vec<i32>) -> i32 {
        (0..target.len()).map(|x| (target[x] - if x > 0{target[x-1]}else {0}).max(0)).sum()
    }
}
// attempt where I tried to do 2 pointer and realized it was much easier than that.
// impl Solution {
//     pub fn min_number_operations(target: Vec<i32>) -> i32 {

//         let (mut a, mut b) = (0, 0);
//         let (mut l, mut r) = (0, target.len() - 1); //next position of l and r
//         let (mut ld, mut rd) = (0, 0); //lowest height we can start at if building from l or r
//         let mini = *target.iter().min().unwrap();
//         let mut count = mini;
//         let target: Vec<i32> = target.into_iter().map(|x| x-mini).collect();
//         println!("{:?}", target);
//         while l < r{
//             println!("ld: {} rd: {} count: {}", ld, rd, count);
//             if ld <= rd{
//                 count += 0.max(target[l] - ld);
//                 if target[l] < ld{ a = target[l]}
//                 ld = target[l];
//                 l += 1;
//             }else{
//                 count += 0.max(target[r] - rd);
//                 if target[r] < rd{ b = target[r]}
//                 rd = target[r];
//                 r -= 1;
//             }
//         }
//         if l != r{return -69}
//         let from_left = (target[l] - ld).max(0);
//         let from_right = (target[r] - rd).max(0);
//         println!("{}, {}, {}, {}, count: {}",from_left, from_right, ld, rd, count);
//         if target[l] <= ld && target[r] <= rd{
//             count
//         }else if target[l] < rd{
//             count - ld + a
//         }else if target[l] < ld{
//             count - rd + b
//         }else{
//             if a > b{
//                 count + target[r] - a + b - rd
//             }else{
//                 count + target[r] - b + a - ld
//             }
//         }
//     }
// }
