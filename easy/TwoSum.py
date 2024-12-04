class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      i,j=0,len(nums)-1
      #create a sorted array with the original indices to return them later.
      nums=sorted([[nums[i],i]for i in range(j+1)])
      #we're guaranteed a solution so while True, else i'd use while i!=j:
      while True:
          #now if we reach the target we'll return the indices
          suma=nums[i][0]+nums[j][0]
          if suma==target:
              return [nums[i][1],nums[j][1]]
          #else if the sum is too large we'll reduce the high number by decreasing j or conversely increase the lower number by increasing i.
          elif suma>target:
              j-=1
          else:
              i+=1
