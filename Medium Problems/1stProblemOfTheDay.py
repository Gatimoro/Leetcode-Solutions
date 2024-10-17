class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        #Each lettah with it's remaining count
        abc=['a',a,'b',b,'c',c]
        happy=''
        #We set index to be the index of the maximum between a, b, and c inside of abc.
        index=abc[1::2].index(max(abc[1::2]))*2+1

        #We can keep going until we have two zeros in a, b and c, 
        #at which point the remaining unknown will equal the sum of all unknowns
        while max(abc[1::2])!=sum(abc[1::2]):
            #here we check that the # of remaining letters isn't 0 and that the last two characters, aren't the letter.
            while abc[index%6] and happy[-2:]!=(2*abc[index%6-1]):
                #if conditions are met, we add the character to our answer and reduce the remaining count.

                happy+=abc[index%6-1]
                abc[index%6]-=1

                #if we just left a large number for a smaller one, we will return to the bigger one on the next iteration.
                index=abc[1::2].index(max(abc[1::2]))*2+1

            #after we are done with one letter, we move to the next
            index+=2
        if happy!='':
            return happy
        #if happy is empty, it could be because we started with 2 zeros already so we just have to add these 1 or 2 characters.
        index=abc[1::2].index(max(abc[1::2]))*2+1
        return (abc[index]*abc[index-1])[:2]
