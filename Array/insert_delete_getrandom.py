import random

class RandomizedSet():
    def __init__(self):
        self.values = []
        self.val_index = {}

    def __insert__(self, val: int) -> bool:
        if self.value in self.val_index:
            return False
        self.value_index[val] = len(self.values)
        self.values.append(val)
        return True

    """{'apple': 0, 'banana': 1, 'cherry': 2}   fruits = ['apple', 'banana', 'cherry']"""
    def remove(self, val: int) -> bool:
        if val not in self.val_index:
            return False
        index = self.val_index[val]
        last_val = self.values[-1]
        self.values[index] = last_val
        self.values.pop()
        self.val_index[last_val] = index
        del self.val_index[val]
        return True


    def get_random(self):
        return random.choice(self.values)
