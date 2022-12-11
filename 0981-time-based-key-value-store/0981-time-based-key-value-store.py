class TimeMap:

    def __init__(self):
        self.dicit = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dicit[key].append((value,timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.dicit[key]
        l = 0 
        r = len(arr) - 1
        best = -1
        while l <= r:
            mid = (l + r)//2
            if arr[mid][1] > timestamp:
                r = mid - 1
            else:
                best = l
                l = mid + 1
        return arr[best][0] if best != -1 else ""
            

        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)