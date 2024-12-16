# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iterative, time complexity O(n), memory complexity O(1)
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         tail = None
#         curr = head

#         while head:
#             curr = head
#             head = head.next
#             curr.next = tail
#             tail = curr
        
#         return curr


# iteratively, time complexcity O(n), memory complexcity O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next =None
        return newHead

# Another iteratively coding, it's easy to understand, time complexcity O(n), memory complexcity O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(prev, cur):
            if not cur:
                return prev

            tail = rec(cur, cur.next)
            cur.next = prev

            return tail
        return self.reverseList(None, head)


