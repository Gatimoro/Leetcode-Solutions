class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int curLen = 0, start = 0, end = 0, cumulative = 0, input_len = nums.size(), ans = 0;
        while(end < input_len){
            if((cumulative & nums[end]) == 0){
                cumulative |= nums[end];
                curLen +=1;
                ans = max(ans, curLen);
                end+=1;
            }else{
                cumulative ^= nums[start];
                start += 1;
                curLen -= 1;
            }
        }
        return ans;
    }
};
// You are given an array nums consisting of positive integers.

// We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

// Return the length of the longest nice subarray.

// A subarray is a contiguous part of an array.

// Note that subarrays of length 1 are always considered nice."""
