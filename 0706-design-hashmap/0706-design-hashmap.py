class MyHashMap:

    def __init__(self):
        self.dict = [[] for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        x = self.dict[key % 10000]
        index = -1
        for idx ,(ky,v) in  enumerate(x):
            if ky == key :
                index = idx
                break
        if index != - 1:
            x[index][1] = value
        else:
            x.append([key,value])

    def get(self, key: int) -> int:
        x = self.dict[key % 10000]
        index = -1
        for idx ,(ky,v) in  enumerate(x):
            if ky == key :
                index = idx
                break
        if index != - 1:
            return x[index][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        x = self.dict[key % 10000]
        index = -1
        for idx ,(ky,v) in  enumerate(x):
            if ky == key :
                index = idx
                break
        if index != - 1:
            del x[index]
        else:
            return -1        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)