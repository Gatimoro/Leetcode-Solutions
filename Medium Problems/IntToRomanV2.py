class Solution:
    def intToRoman(self, num: int) -> str:
        ans=''
        guan=["","I",'II','III',"IV",'V','VI','VII',"VIII","IX"]
        chu=["","X",'XX','XXX',"XL",'L','LX','LXX',"LXXX","XC"]
        tree=["","C",'CC','CCC','CD','D','DC','DCC','DCCC','CM']
        cuatro=["","M","MM",'MMM']
        romans=[guan,chu,tree,cuatro]
        c=0
        while num:
            ans=romans[c][num%10]+ans
            c+=1
            num=num//10
        return ans
