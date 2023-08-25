class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        i = 0
        while s[i] == s[len(s) - 1 - i]:
            i += 1
            
        s1 = s[:i] + s[i + 1:]
        s2 = s[:len(s) - 1 - i] + s[len(s) - i:]
        
        if s1 == s1[::-1] or s2 == s2[::-1]:
            return True
        
        return False