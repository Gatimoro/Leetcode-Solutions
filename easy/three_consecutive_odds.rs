//determine if there are 3 consecutive odds in the array.
impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        arr.into_iter().fold((false, 0), |(found, cur), x|{ if found{ (true, 0) }else if x % 2 == 1{ (cur == 2, cur + 1) }else{ (false, 0) } } ).0
    }
}
