class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cock=1
        ansa=[]
        #when k is 1, we return the original list as each element is a subsequence of len 1
        if k==1:
            return nums
        #we check first k terms for sequence and record the current consecutive seq length
        for flumbus in range(1,k):
            if nums[flumbus]==nums[flumbus-1]+1:
                cock+=1
            else:
                cock=1
        #if the first k terms were consecutive, cock equals k
        if cock == k:
            ansa.append(nums[k-1])
        #if not, we shall append 1
        else:
            ansa.append(-1)
        #we go throgh the whole list, starting at k
        for grrrr in range(k,len(nums)):
            #whenever the number equals the previous plus 1,
            if nums[grrrr]==nums[grrrr-1]+1:
                cock+=1
                #we check if the consecutive increasing sequence before it is k or longer.
                if cock>=k:
                    #in which case we append the last number in it, ie nums[grrrr]
                    ansa.append(nums[grrrr])
                #else we just append -1
                else:
                    ansa.append(-1)
            #when the number isn't = last+1, we restart the count, which i called cock for some reason.
            else:
                ansa.append(-1)
                if cock!=1:
                    cock=1
        return ansa



