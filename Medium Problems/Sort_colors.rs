//Sort colors denoted 0, 1 and 2 in ascending order.
impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let (mut i, mut nz, mut nt) = (0, 0, nums.len() - 1);

        while i <= nt{
            if nums[nz] == 0{
                nz += 1;
                if nz == nums.len(){
                    return
                }
                i = i.max(nz);
            }else if nums[nt] == 2{
                if nt == 0{
                    return;
                }
                nt -= 1;
            }else if nums[i] == 0{
                nums[i] = nums[nz];
                nums[nz] = 0;
                nz += 1;
            }else if nums[i] == 2{
                nums[i] = nums[nt];
                nums[nt] = 2;
                nt -= 1
            }else{
                i += 1;
            }
        } 
    }
}
