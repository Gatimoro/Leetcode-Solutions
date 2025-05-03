use std::collections::HashSet;
impl Solution {
    pub fn min_domino_rotations(tops: Vec<i32>, bottoms: Vec<i32>) -> i32 {
        let mut tcount = [0,0];//how many swaps to complete top row, bottom row with tops[0]
        let mut bcount = [0,0];//same for bottoms[0].

        let mut valid = [tops[0],bottoms[0]];
        for (top, bot) in tops.into_iter().zip(bottoms.into_iter()){
            
            let (t0, t1) = (valid[0] != top, valid[0] != bot);
            let (b0, b1) = (valid[1] != top, valid[1] != bot);

            if  (t0 && t1){
                valid[0] = -1;
            }else{
                tcount[0] += t0 as i32;
                tcount[1] += t1 as i32;
            }

            if  (b0 && b1){
                valid[1] = -1;
            }else{
                bcount[0] += b0 as i32;
                bcount[1] += b1 as i32;
            }

            // println!("{:?}{:?},{:?}", tcount, bcount,valid);


            if valid[1] == -1 && valid[0] == -1{
                return -1;
            }
        }
        if valid[0] != -1{
            return tcount[0].min(tcount[1]);
        }bcount[0].min(bcount[1])
    }
}

// In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

// We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

// Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

// If it cannot be done, return -1.
