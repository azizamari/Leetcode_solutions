class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        while True:
            if i < 0:
                digits=[0]+digits
                i=0
            digits[i]+=1
            if digits[i]==10:
                digits[i]=0
                i-=1
            else:
                break
        return digits