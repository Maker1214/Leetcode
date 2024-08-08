class MinStack:

    def __init__(self):
        self.s1 = [] # origianl stack and you will push val into this stack
        self.s2 = [] # restore current minimum val
        

    def push(self, val: int) -> None:
        self.s1.append(val)
        self.s2.append(min(val, self.s2[-1] if len(self.s2) else val))

    def pop(self) -> None:
        self.s2.pop()
        print(f"pop value is {self.s1.pop()}")

    def top(self) -> int:
        return self.s1[-1]
        

    def getMin(self) -> int:
        return self.s2[-1]


# Methods pop, top and getMin operations will always be called on non-empty stacks.
# Your MinStack object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MinStack()
    obj.push(2)
    obj.push(5)
    obj.push(9)
    obj.push(8)
    obj.push(1)
    obj.push(4)
    print(obj.getMin())
    obj.pop()
    obj.pop()
    print(obj.getMin())

    
