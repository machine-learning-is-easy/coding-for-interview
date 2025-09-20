
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size
    def _index(self, key: int) -> int:
        return key % self.size
    def put(self, key: int, value: int) -> None:
        idx = self._index(key)
        if not self.table[idx]:
            self.table[idx] = ListNode(key, value)
            return
        current = self.table[idx]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                current.next = ListNode(key, value)
                return
            current = current.next
    def get(self, key: int) -> int:
        idx = self._index(key)
        current = self.table[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._index(key)
        current = self.table[idx]
        if not current:
            return
        if current.key == key:
            self.table[idx] = current.next
            return
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next