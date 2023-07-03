# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0: return None
        l=PriorityQueue()
        n=0
        for i in lists:
            curr=i
            while curr:
                l.put(curr.val)
                n+=1
                curr=curr.next
        if n==0: return None
        res_head=ListNode(l.get())
        res_curr=res_head
        n-=1
        while n>0:
            n-=1
            print(l.qsize())
            res_curr.next=ListNode(l.get())
            res_curr=res_curr.next
        return res_head



        