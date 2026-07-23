# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head 
        while curr:
            count += 1
            curr = curr.next
        if count == 1 and n == 1:
            return None
        rem = count - n
        if rem == 0:
            return head.next
        print(rem)
        curr = head
        count = 0
        while curr:
            if count + 1 == rem:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1
        return head
        