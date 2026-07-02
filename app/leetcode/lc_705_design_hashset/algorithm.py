class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.data = [[] for i in range(self.size)]

    def add(self, key: int) -> None:
        index = key % self.size
        for num in self.data[index]:
            if num == key:
                return None
        self.data[index].append(key)
        return None

    def remove(self, key: int) -> None:
        index = key % self.size
        i = 0
        for num in self.data[index]:
            if num == key:
                del self.data[index][i]
                return None
            i += 1
        return None

    def contains(self, key: int) -> bool:
        index = key % self.size
        for num in self.data[index]:
            if num == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
