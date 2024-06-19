class ListNode():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def create_linked_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for i in range(len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next

    return dummy.next

def reverse_linked_list(node):
    cur = None
    tail = node
    
    while tail:
        pre = cur
        cur = tail
        tail = tail.next
        cur.next = pre
    
    return cur

nums = [8,4,2,9,7]
head = create_linked_list(nums)

fast = slow = head

while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

mid = slow
tail = reverse_linked_list(slow)
dummy = ListNode(None)
dummy.next = head
curr = head

while head != mid:
    if curr == head:
        head = head.next
        curr.next = tail
    else:
        tail = tail.next
        curr.next = head
    curr = curr.next

n = dummy.next
while n:
    print(n.val)
    n = n.next



    






