# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = ListNode(0)
        curr = new_head
        while True:
            next_node = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if next_node == -1 or lists[next_node].val > lists[i].val:
                    next_node = i
            if next_node == -1:
                break
            curr.next = lists[next_node]
            lists[next_node] = lists[next_node].next
            curr = curr.next
        return new_head.next


