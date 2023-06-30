# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l=[]
        cur=head
        while cur!=None:
            l.append(cur)
            cur=cur.next
        n=len(l)
        for i in range(n//2):
            l[i].next=l[n-1-i]
            l[n-1-i].next=l[i+1]
            print(l[i].next.val,l[n-1-i].next.val)
        l[n//2].next=None