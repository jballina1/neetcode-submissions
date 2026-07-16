# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0
        curr = head
        while curr:
            list_length += 1 
            curr = curr.next
        node_to_remove = list_length - n + 1
        if node_to_remove == 1:
            return head.next
        node_num = 1
        curr = head
        while curr:
            if node_num == node_to_remove - 1:
                temp = curr.next.next
                curr.next = temp
                break
            node_num += 1
            curr = curr.next
        return head
                