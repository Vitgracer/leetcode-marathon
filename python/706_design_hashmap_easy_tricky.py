"""
https://leetcode.com/problems/design-hashmap/description/
"""

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_val = self._hash(key)
        bucket = self.buckets[hash_val]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = key, value
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        hash_val = self._hash(key)
        bucket = self.buckets[hash_val]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hash_val = self._hash(key)
        bucket = self.buckets[hash_val]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]