# Design your implementation of the circular queue. 
# The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, 
# and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
# In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. 
# But using the circular queue, we can use the space to store new values.

# Implement the MyCircularQueue class:

# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language. 

 

# Example 1:

# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]

# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4
 

# Constraints:

# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

# 這個enQueue的方式只有當到達最大長度時才將head跟tail連起來
# class ListNode:
#     def __init__(self,val,pre,nxt):
#         self.val = val
#         self.pre = pre
#         self.nxt = nxt

# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.maxiLen = k
#         self.currLen = 0
#         self.head = self.tail = ListNode(None,None,None)
    
#     def enQueue(self, value: int) -> bool:
#         if self.currLen + 1 > self.maxiLen: return False
#         if self.currLen != 0:
#             temp = ListNode(value,self.tail,None)
#             self.tail.nxt = temp
#             self.tail = temp
#             if self.currLen == self.maxiLen:
#                 self.tail.nxt, self.head.pre = self.head, self.tail
#         else:
#             self.head = self.tail = ListNode(value,None,None)
#         self.currLen += 1
#         return True
        
#     def deQueue(self) -> bool:
#         if self.currLen <= 0: return False
#         if self.currLen != 1:
#             if self.currLen == self.maxiLen:
#                 self.tail.nxt = self.head.pre = None
#             self.head = self.head.nxt
#             self.head.pre = None
#         else:
#             self.head = self.tail = ListNode(None,None,None)
#         self.currLen -=1
#         return True
        
#     def Front(self) -> int:
#         return self.head.val if self.currLen else -1

#     def Rear(self) -> int:
#         return self.tail.val if self.currLen else -1

#     def isEmpty(self) -> bool:
#         return True if self.currLen == 0 else False 

#     def isFull(self) -> bool:
#         return True if self.currLen == self.maxiLen else False

#     def prinAll(self):
#         dummy = self.head
#         tempLen = self.currLen
#         while tempLen:
#             print(dummy.val)
#             dummy = dummy.nxt
#             tempLen -= 1


# 使用兩個dummy nodes，一個在最前面(head)，一個在最後面(tail)，如下所式，所有的enqueue和dequeue都在head與tail之間進行，例如enqueue(1)，但是這種作法不算是真正的circular queue。
# None <- head -> <-  tail -> None == enqueue(1) ==> None <- head -> <- 1 -> <-  tail -> None
# class ListNode:
#     def __init__(self,val,pre,nxt):
#         self.val = val
#         self.pre = pre
#         self.nxt = nxt


# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.space = k
#         self.head = ListNode(0, None, None)
#         self.tail = ListNode(0, self.head, None)
#         self.head.nxt = self.tail

#     def enQueue(self, value: int) -> bool:
#         if self.isFull(): return False
#         curr = ListNode(value, self.tail.pre, self.tail)
#         self.tail.pre.nxt = curr
#         self.tail.pre = curr
#         self.space -= 1
#         return True
    
#     def deQueue(self) -> bool:
#         if self.isEmpty(): return False
#         self.head.nxt.nxt.pre = self.head
#         self.head.nxt = self.head.nxt.nxt
#         self.space += 1
#         return True

#     def Front(self) -> int:
#         return -1 if self.isEmpty() else self.head.nxt.val
    
#     def Rear(self) -> int:
#         return -1 if self.isEmpty() else self.tail.pre.val

#     def isEmpty(self) -> bool:
#         return self.head.nxt == self.tail
    
#     def isFull(self) -> bool:
#         return self.space == 0
    
#     def printAll(self):
#         temp = self.head.nxt
#         while temp != self.tail:            
#             print(temp.val)
#             temp = temp.nxt

# 使用list搭配len可達成circular queue
class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.front = 0
        self.end = -1
        self.qSize = 1000
        self.queue = [0] * self.qSize        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.end += 1
        self.queue[self.end % self.qSize] = value
        self.space -= 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.front += 1
        self.space += 1
        return True
        

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front % self.qSize]
        

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.end % self.qSize]
        

    def isEmpty(self) -> bool:
        return self.space != 0 and self.front - self.end == 1
        

    def isFull(self) -> bool:
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(4)
print(obj.Rear())
print(obj.isFull())
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.Rear())

# param_5 = obj.isEmpty()
# param_6 = obj.isFull()