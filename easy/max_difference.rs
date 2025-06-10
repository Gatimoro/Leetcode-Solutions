impl Solution {
    pub fn max_difference(s: String) -> i32 {
        let mut freq = [0; 26];
        let (mut max_even, mut max_odd, mut min_even, mut min_odd, mut ans) = (0, 0, i32::MAX, i32::MAX, 0);
        for l in s.into_bytes(){
            let idx = (l - b'a') as usize;
            freq[idx] += 1;
        }
        for f in freq{
            if f == 0{
                continue;
            }
            if f%2 == 0{
                min_even = min_even.min(f);
                max_even = max_even.max(f);
            }else{
                min_odd = min_odd.min(f);
                max_odd = max_odd.max(f);
            } // println!("{} {} {} {}", max_odd, max_even, min_odd, min_even);
        }
        (max_odd - min_even)
            
    }
}
