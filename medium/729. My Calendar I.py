# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

# Constraints:

# 0 <= start < end <= 109
# At most 1000 calls will be made to book.

#Brute Force : O(n * m), n is the len(self.calendar), m is the number of booking
# class MyCalendar:

#     def __init__(self):
#         self.calendar = []
        
#     def book(self, startTime: int, endTime: int) -> bool:
#         for s, e in self.calendar:
#             if endTime > s and startTime < e:                
#                 return False
#         self.calendar.append([startTime, endTime])
#         return True

# Binary Tree : O(m * log n)
# recursive
class treeNode:
    def __init__(self, s: int, e: int):
        self.start = s
        self.end = e
        self.left = None
        self.right = None

class MyCalendar:
    def __init__(self):
        self.root = None
    
    def book(self, startTime: int, endTime: int) -> bool:
        print(f"check {startTime, endTime}")
        if not self.root:
            self.root = treeNode(startTime, endTime)
            return True            
        return self.insert(self.root, startTime, endTime)       

    def insert(self, node, startTime, endTime) -> bool:
        print(f"curr node is {node.start, node.end}")
        if startTime < node.end and endTime > node.start: # the time period was booked
            print(f"the time period was booked")
            return False
        if endTime <= node.start: # find the left tree
            print(f"find the left tree")
            if not node.left:
                node.left = treeNode(startTime, endTime)
                return True
            return self.insert(node.left, startTime, endTime)            
        else: # find the right tree
            print(f"find the rght tree")
            if not node.right:
                node.right = treeNode(startTime, endTime)
                return True
            return self.insert(node.right, startTime, endTime)
        
# iterative
# class treeNode:
#     def __init__(self, s: int, e: int):
#         self.start = s
#         self.end = e
#         self.left = None
#         self.right = None
    
#     def insert(self, startTime: int, endTime: int) -> bool:
#         curr = self
#         while True:
#             #print(f"curr is {curr.start, curr.end}")
#             if endTime <= curr.start: 
#                 #print(f"find left")                
#                 # find left tree
#                 if not curr.left:
#                     curr.left = treeNode(startTime, endTime)
#                     return True
#                 curr = curr.left                                    
#             elif startTime >= curr.end:
#                 #print(f"find right")
#                 # find right tree
#                 if not curr.right:
#                     curr.right = treeNode(startTime, endTime)
#                     return True
#                 curr = curr.right
#             else:
#                 return False

# class MyCalendar:
#     def __init__(self):
#         self.root = None

#     def book(self, startTime: int, endTime: int) -> bool:
#         #print(f"book is {startTime, endTime}")
#         if not self.root:
#             self.root = treeNode(startTime, endTime)
#             return True
#         return self.root.insert(startTime, endTime)
        


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(47,50))
print(obj.book(33,41))
print(obj.book(39,45))
print(obj.book(33,42))
print(obj.book(25,32))
print(obj.book(26,35))
print(obj.book(19,25))
print(obj.book(3,8))
print(obj.book(8,13))
print(obj.book(18,27))


