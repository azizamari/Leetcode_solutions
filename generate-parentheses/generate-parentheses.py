class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def generate(n,m,x):
            if n==m==0:
                res.append(x)
            elif n==m:
                generate(n-1,m,x+'(')
            elif n==0 and m!=0:
                generate(n,m-1,x+')')
            elif m==0 and n!=0:
                return
            else:
                generate(n,m-1,x+')')
                generate(n-1,m,x+'(')
        generate(n,n,'')
        return res

            