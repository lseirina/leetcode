class CustomStack:
    def __init__(self):
        self.max_val = []
        self.values = []
    """[3, 5, 2, 8]
        [3, 5, 8]
    """
    def push(self, val: int):
        self.values.append(val)
        if not self.max_val or val >= self.max_val[-1]:
            self.max_val.append(val)

    def pop(self):
        if not self.values:
            return -1
        val = self.values.pop()
        if val == self.max_val[-1]:
            self.max_val.pop()
        return val


    def top(self):
        if not self.values:
            return -1
        return self.values[-1]

    """[3, 5, 2, 8]"""
    def getMax(self):
        if not self.values:
            return -1
        return self.max_val[-1]


stack = CustomStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(8)
print(stack.getMax())
stack.pop()
print(stack.getMax())