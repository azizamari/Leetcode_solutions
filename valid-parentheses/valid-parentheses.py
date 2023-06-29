class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                l.append(i)
            else:
                if len(l)!=0 and ((i==')' and l[-1]=='(') or (i =='}' and l[-1]=='{') or (i ==']' and l[-1]=='[')):
                    l.pop()
                else: 
                    return False
        return l==[]