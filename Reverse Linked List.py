class ListNode():
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

def reverse_linked_list(node):

    cur = None
    tail = node

    while tail:
        pre = cur
        cur = tail
        tail = tail.next
        cur.next = pre
    return cur
        

def create_linked_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for i in range(len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next

    return dummy.next


nums = [8,4,2,9,7]
head = create_linked_list(nums)
present = head
while present:
    print(f"反轉前:{present.val}")
    present = present.next

reversed_linked_list = reverse_linked_list(head)

while reversed_linked_list:
    print(f"反轉後:{reversed_linked_list.val}")
    reversed_linked_list = reversed_linked_list.next








