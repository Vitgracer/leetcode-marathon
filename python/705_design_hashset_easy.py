"""
https://leetcode.com/problems/design-hashset/
"""

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)] 

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hash_val = self._hash(key)
        bucket = self.buckets[hash_val]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        hash_val = self._hash(key)
        bucket = self.buckets[hash_val]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        hash_val = self._hash(key)
        bucket = self.buckets[hash_val]
        if key in bucket:
            return True
        return False