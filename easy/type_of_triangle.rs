impl Solution {
    pub fn triangle_type(mut nums: Vec<i32>) -> String {
        nums.sort();
        if nums[2] >= nums[0] + nums[1]{
            return String::from("none");
        }
        nums.dedup();
       
        match nums.len(){
            1 => {String::from("equilateral")}
            2 => {String::from("isosceles")}
            _ => {String::from("scalene")}
        }
    }
}
