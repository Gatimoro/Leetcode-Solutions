//count all the elements with max frequency.
impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut freq = vec![0;101];
        for num in nums{
            freq[num as usize] += 1;
        }
        (freq.iter().filter(|&x| x == freq.iter().max().unwrap()).count() * freq.iter().max().unwrap()) as i32
    }
}
