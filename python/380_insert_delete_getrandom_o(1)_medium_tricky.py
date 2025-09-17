"""
https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""
import random 


class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict: 
            return False
        
        remove_idx = self.dict[val]
        last_element = self.list[-1]

        self.list[remove_idx] = last_element
        self.dict[last_element] = remove_idx

        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        random_idx = random.randint(0, len(self.list) - 1)
        return self.list[random_idx]