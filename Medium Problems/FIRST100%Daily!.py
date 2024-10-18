class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        liza=[]
        leng=jumbo=ansa=0
        garbanzo=1
        #transfer numbers to list. note that this reverses their order.
        while num:#until we run out of number:
            dig=num%10 #get digit
            liza.append(dig) #add digit to list
            num=num//10 #go to next number
            leng+=1 #get length
        for x in range(leng-1,0,-1):#list[len(list)] is a common pain, x is the index of the leading number 
            for y in range (x):#and y the index of every one to the right of it.
                if liza[y]>liza[x] and liza[y]>jumbo:
                    jumbo=liza[y]#store the largest value
                    leng=y #recycle leng to store the index
            if jumbo:#once we find a match
                liza[leng]=liza[x]#leng is the index of the bigger number to the right
                liza[x]=jumbo#x the leading smaller number
                break #exit the loop
        for alfredo in liza:#for each number in the list, 
            ansa+=alfredo*garbanzo #we pretty much do the opposite as in the first section
            garbanzo=garbanzo*10 #The garbanzo grows 10x it's size with each iteration.
        return ansa
