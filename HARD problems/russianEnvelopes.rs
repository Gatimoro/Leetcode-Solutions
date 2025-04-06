// You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

// One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

// Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

// Note: You cannot rotate an envelope.
impl Solution {
    pub fn max_envelopes(mut envelopes: Vec<Vec<i32>>) -> i32 {
        envelopes.sort_by(|a, b| {
            if a[0] == b[0]{
                b[1].cmp(&a[1])
            }else{
                a[0].cmp(&b[0])
            }
        });
        
        fn position(x:i32, arr: &Vec<i32>) -> usize{
            let (mut l, mut mid, mut r) = (0, 0, arr.len());

            while l<r{
                let mid = (l + r) >> 1;
                if arr[mid] >= x{
                    r = mid;
                }else{
                    l = mid + 1;
                }
            }l
        }

        let mut seq = Vec::<i32>::with_capacity(envelopes.len());
        let mut find_insert = 0;
        for envelope in envelopes.into_iter(){
            find_insert = position(envelope[1], &seq);
            if find_insert == seq.len(){
                seq.push(envelope[1])
            }else{
                seq[find_insert] = envelope[1];
            }

        }seq.len() as i32
    }
}
