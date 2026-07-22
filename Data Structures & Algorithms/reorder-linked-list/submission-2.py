class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        pivot = head

        while pivot and pivot.next:
            prev = None
            curr = pivot
            while curr.next:
                prev = curr
                curr = curr.next
            if pivot == curr:
                break
            if pivot.next == curr:
                break
            aux = pivot.next
            pivot.next = curr
            curr.next = aux
            prev.next = None
            pivot = aux