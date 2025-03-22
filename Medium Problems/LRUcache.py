"""Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity."""
class LRUCache:

    def __init__(self, capacity: int):
        self.logs = deque()
        self.vals = dict()
        self.remaining = capacity
        self.time = 0

    def get(self, key: int) -> int:
        if key not in self.vals: return -1
        
        self.time += 1 
        self.logs.append((key,self.time))
        self.vals[key][1] = self.time
        return self.vals[key][0]

    def put(self, key: int, value: int) -> None:
        self.time+=1
        
        self.logs.append((key,self.time))
        if key in self.vals:
            self.vals[key] = [value, self.time]
            return
        self.vals[key] = [value, self.time]
            
        if self.remaining:
            self.remaining -= 1
            return
        while True:
            cand, time = self.logs.popleft()
            if self.vals[cand][1] == time:
                break
        del self.vals[cand]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
