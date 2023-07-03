class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        current = head
        next = None
        prev = None
        count = 0
        node_count = 0
        temp = head
        while temp is not None and node_count < k:
            temp = temp.next
            node_count += 1
        if node_count < k:
            return head
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverseKGroup(next, k)
        return prev
