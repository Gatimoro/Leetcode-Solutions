class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]   SO BASICALLY WE HAVE A STRUCTURE OF BLOCKS OF HEIGHT height[index] AND WE CALCULATE THE RAINFALL
        :rtype: int                      THAT SAID STURCTURE RETAINS IN UNITS SQUARED, WHERE HEIGHT IS GIVEN IN UNITS  
        """
        top=height.index(max(height))
        trap=0
        for oogabooga in range (2): #there are 2 sides to a mountaintop
            hold=i=0
            while i < top:      #while we haven't reached the mountain top, each time we have a dip from
#the highest water level before that, the dip is guaranteed to be filled
                if height[i]>hold:#but if we find a higher place than the water level, we reasign it to again.
                    hold=height[i]
                else:
                    trap+=hold-height[i]
                i+=1
            if oogabooga: #after the second iteration, oogabooga=1, id est True.
                return trap
            height=height[::-1] #after the first iteration, we reverse the mountain and calculate the water on the other side.
            top=len(height)-1-top
