class NumberContainers:
    def __init__(self):
        self.container={}
        self.appears = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        #check if the number's place is occupied
        if index in self.container:
            last_val = self.container[index]
            
            #if it's a new value, remove index, from last value's indexes
            if last_val != number: 
                self.appears[last_val].pop(bisect.bisect_left(self.appears[last_val],index))
                bisect.insort(self.appears[number],index)
        else:
            bisect.insort(self.appears[number],index)
        self.container[index]=number

    def find(self, number: int) -> int:
        if self.appears[number]:
            return self.appears[number][0] 
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
