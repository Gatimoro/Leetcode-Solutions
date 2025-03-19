class Solution {
public:
    int minOperations(vector<int>& nums) {
        int leng = nums.size() - 2;
        int c = 0;
        for(int i = 0; i < leng; i++){
            if(nums[i] == 0){
                for(int di = 0; di<3; di++){
                    nums[i + di] ^= 1;
                }
                c++;
            }
        }return (nums[leng-1] == 1 && nums[leng+1] == 1 && nums[leng] == 1) ? c : -1;
    }
};
// You are given a binary array nums.

// You can do the following operation on the array any number of times (possibly zero):

// Choose any 3 consecutive elements from the array and flip all of them.
// Flipping an element means changing its value from 0 to 1, and from 1 to 0.

// Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
