// You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, where obstacles[i] describes the height of the ith obstacle.

// For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course in obstacles such that:

// You choose any number of obstacles between 0 and i inclusive.
// You must include the ith obstacle in the course.
// You must put the chosen obstacles in the same order as they appear in obstacles.
// Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.
// Return an array ans of length n, where ans[i] is the length of the longest obstacle course for index i as described above.

 
use std::collections::HashMap;
impl Solution {
    pub fn longest_obstacle_course_at_each_position(obstacles: Vec<i32>) -> Vec<i32> {
        let mut order = HashMap::new();
        let (mut i, mut ord, mut last) = (0, 1, -1);
        let mut sorted = obstacles.clone();
        sorted.sort();
        while i < sorted.len() {
            if sorted[i] != last {
                last = sorted[i];
                order.insert(sorted[i], ord);
                ord += 1;
            }
            i += 1;
        }
        let mut feinwick:Vec<i32> = vec![0;ord];
        fn update(arr: &mut Vec<i32>, mut val: isize, sweet: i32){
            arr[val as usize] = sweet;
            val += val & -val; 
            while (val as usize) < arr.len() && sweet > arr[val as usize]{
                arr[val as usize] = sweet;
                val += val & -val; 
            }
        }
        fn longest_in(arr: &Vec<i32>, mut val: isize) -> i32{
            let mut sweet = arr[val as usize];
            val -= val & -val; 
            while val > 0 {
                sweet = sweet.max(arr[val as usize]); 
                val -= val & -val; 
            }sweet as i32
        }
        let mut ans = Vec::with_capacity(obstacles.len());
        for obstacle in obstacles.iter(){
            let obs = order.get(obstacle).unwrap();
            let sw = longest_in(&feinwick, *obs as isize)+1;
            ans.push(sw);
            update(&mut feinwick, *obs as isize, sw);
        }
        ans
    }
}
