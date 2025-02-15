class ProductOfNumbers:

    def __init__(self):
        self.prods=[1]
        self.lzero=-1

    def add(self, num: int) -> None:
        if num!=0:self.prods.append(self.prods[-1]*num)
        else: 
            self.prods.append(1)
            self.lzero=len(self.prods)
            

    def getProduct(self, k: int) -> int:
        if self.lzero > len(self.prods) - k: return 0
        return self.prods[-1]//self.prods[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
"""Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing."""
