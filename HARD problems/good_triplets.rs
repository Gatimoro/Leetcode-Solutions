// You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

// A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

// Return the total number of good triplets.
impl Solution {
    pub fn good_triplets(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let length = nums1.len();

        fn less_than(arr: &Vec<i32>, mut x: usize) -> i32 {  
            let mut count = 0;
            while x > 0 && x<arr.len(){
                count += arr[x];
                x -= (x as i32 & -(x as i32)) as usize;
            }
            count
        }

        fn update_lower(arr: &mut Vec<i32>, mut x: usize) {  
            x += 1;
            while x < arr.len() {
                arr[x] += 1;
                x += (x as i32 & -(x as i32)) as usize;
            }
        }

        fn greater_than(arr: &Vec<i32>, mut x: usize) -> i32 {  
            if x == 0 {
                return 0;
            }
            let mut count = 0;
            while x < arr.len() {
                count += arr[x];
                x += (x as i32 & -(x as i32)) as usize;
            }
            count
        }

        fn update_higher(arr: &mut Vec<i32>, mut x: usize) {  
            x -= 1;
            while x > 0 && x < arr.len(){
                arr[x] += 1;
                x -= (x as i32 & -(x as i32)) as usize;
            }
        }

        let mut indices = vec![0; length];
        for (i, num) in nums2.into_iter().enumerate() {
            indices[num as usize] = i;
        }

        let the_arr: Vec<usize> = nums1.into_iter().map(|x| indices[x as usize]).collect();
        let mut under = Vec::with_capacity(length);

        let mut the_number = vec![0; length + 1];

        for &numba in the_arr.iter() {
            under.push(less_than(&the_number, numba));
            update_lower(&mut the_number, numba);
        }

        let mut above = vec![0; length];
        let mut the_number = vec![0; length + 1];

        for (i, &numba) in the_arr.iter().enumerate().rev() {
            above[i] = greater_than(&the_number, numba);
            update_higher(&mut the_number, numba);
        }

        let mut ret = 0;
        for index in 1..length - 1 {
            ret += under[index] as i64 * above[index] as i64;
        }

        ret
    }
}

