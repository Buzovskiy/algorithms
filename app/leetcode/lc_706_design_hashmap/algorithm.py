class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.data = [[] for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        for kv in self.data[index]:
            if kv[0] == key:
                kv[1] = value
                return None
        self.data[index].append([key, value])
        return None

    def get(self, key: int) -> int:
        index = key % self.size
        for kv in self.data[index]:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        i = 0
        for kv in self.data[index]:
            if kv[0] == key:
                del self.data[index][i]
                return None
            i += 1
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
