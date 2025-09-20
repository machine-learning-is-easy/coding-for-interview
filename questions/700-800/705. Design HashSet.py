

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.size = 1000  # Define the size of the hash table
        self.buckets = [None] * self.size  # Create an array of empty buckets

    def _hash(self, key):
        return key % self.size  # Simple modulo-based hash function

    def add(self, key: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key)
        else:
            current = self.buckets[index]
            while True:
                if current.key == key:
                    return  # Key already exists, do nothing
                if not current.next:
                    break
                current = current.next
            current.next = ListNode(key)  # Append new node

    def remove(self, key: int) -> None:
        index = self._hash(key)
        current = self.buckets[index]
        if not current:
            return  # Key not found
        if current.key == key:
            self.buckets[index] = current.next  # Remove head node
            return
        prev = None
        while current:
            if current.key == key:
                prev.next = current.next  # Remove node
                return
            prev, current = current, current.next

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)