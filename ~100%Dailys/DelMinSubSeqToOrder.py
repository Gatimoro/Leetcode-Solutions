class Solution:
  """ I HAVE BEEN ON VACATION FOR A COUPLE OF DAYS WITHOUT ACCESS TO A WORTHY COMPUTER, BUT NOW I'M BACK AND I AM STRONGER """
  """ THE GOAL OF THIS PROGRAM IS TO RETURN THE LENGTH OF THE SHORTEST SUBSEQUENCE YOU NEED TO REMOVE IN ORDER TO MAKE THE LIST arr SORTED"""
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        #We start with calculating for how long the sequence is ordered from first (ff) and from last (fl)
        fl=-1
        ff=0
        m=len(arr)
        #check from last
        while m+fl>0 and arr[fl]>=arr[fl - 1]:
            fl-=1
        #if the sequence is completely ordered, return 0 as there is nothing to remove
        if fl==-m:
            return 0
        #now check from first
        while ff<m-1 and arr[ff]<=arr[ff+1]:
            ff+=1
        #ds is the space between ff and fl, so the bare minimum subsequence we will have to remove
        ds=m-1-ff+fl
        #in a perfect world, after the ds break, the next term is larger than the last ordered item, we check for this
        if arr[ff]<arr[fl]:
            return ds
        itero=1
        #since we don't live in a perfect world, we check removing substrings of increasing length until we found one solution. Since we start from removing the minimum substring and go up, the first solution we find will be the (one of) the shortest substings we can remove. We only care about the length of said substing and hence we return it.
        while True:
            for i in range(itero+1):
                i2=fl+itero-i
                i1=ff-i
                #notice here, how when we have a substring that appended to one of the ordered from first or from last substring, combines to a length greater than that of arr, we can just remove everything but the longer ordered substring, be it ff or fl. 
                if i1<0 or i2>=0 or arr[i1]<=arr[i2]:
                    return ds+itero
            #itero is my gamba inspired iteration counter.
            itero+=1

        
