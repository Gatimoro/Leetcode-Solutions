// There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

// You are giving candies to these children subjected to the following requirements:

// Each child must have at least one candy.
// Children with a higher rating get more candies than their neighbors.
// Return the minimum number of candies you need to have to distribute the candies to the children.
impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let n = ratings.len();
        let mut candies = vec![1; n];
        
        
        for i in 1..n {
            if ratings[i] > ratings[i - 1] {
                candies[i] = candies[i - 1] + 1;
            }
        }
        for i in (0..n - 1).rev() {
            if ratings[i] > ratings[i + 1] {
                candies[i] = candies[i].max(candies[i + 1] + 1);
            }
        }

        candies.iter().sum()
    }
}

// impl Solution {
//     pub fn candy(ratings: Vec<i32>) -> i32 {
//         let n = ratings.len();
//         let mut sol = vec![1; n];
//         let mut prev = -1;
//         let mut count = 1;
//         for i in 0..n{
//             if ratings[i] <= prev{
//                 count = 1;
//             }
//             prev = ratings[i];
//             sol[i] = count;
//             count += 1;
//         }
//         println!("{:?}", sol);

//         for i in (0..n).rev(){
//             if sol[i] == 1 && ratings[i] > prev{
//                 count += 1;
//                 sol[i] = count;
//             }else{
//                 count = 1;
//             }
//             prev = ratings[i];
//         }
//         println!("{:?}", sol);
        
//         let mut ret = 0;
//         for i in (1..n - 1){
//             if ratings[i-1] < ratings[i] && ratings[i] > ratings[i + 1]{
//                 //sol[i] = sol[i-1].max(sol[i + 1]) + 1;
//                 ret += sol[i + 1].max(sol[i - 1]) + 1;
//             }else{
//                 ret += sol[i]

//             }
//         }
//         println!("{:?}", sol);
//         ret + sol[0] + sol[sol.len() - 1]
        
//     }
// }
