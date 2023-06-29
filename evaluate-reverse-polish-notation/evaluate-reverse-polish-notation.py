class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            try:
                val=int(token)
                stack.append(val)
            except:
                x=stack.pop()
                y=stack.pop()
                res=0
                if token=='+':res=y+x
                elif token=='-': res=y-x
                elif token=='/':res=int(y/x)
                elif token=='*':res=y*x
                stack.append(res)
        return stack[0]