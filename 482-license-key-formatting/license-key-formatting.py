class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result=''
        c=0
        for i in range(len(s)):
            if s[len(s)-i-1]=='-': continue 
            result=s[len(s)-i-1].upper()+result
            c+=1
            if c==k: 
                result='-'+result
                c=0
        if (len(result) > 0 and result[0] == '-'):
            result = result[1:]
        return result
            
