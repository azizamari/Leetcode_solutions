"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None: return None
        new_head=Node(head.val)
        cur=head
        new_cur=new_head
        garbage=[]
        wasnone=False
        while not wasnone:
            new_cur.val=cur.val
            new_cur.random=cur.random
            garbage.append(cur)
            temp=cur
            cur=cur.next
            if temp.next!=None:
                new_cur.next=Node(-1)
            wasnone=temp.next==None
            temp.next=new_cur
            new_cur=new_cur.next
        cur=head
        new_cur=new_head
        while new_cur:
            if new_cur.random:
                new_cur.random=new_cur.random.next
            new_cur=new_cur.next
        return new_head