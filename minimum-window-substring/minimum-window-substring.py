class Solution:
    def isValid(self,hmap, org):
        cnt = 0

        for i, j in hmap.items():
            if i in org and j >= org[i]:
                cnt += 1

        if (cnt != len(org)):
            return False

        return True
    def minWindow(self, s: str, t: str) -> str:
        if (len(s) < len(t)):
            return ""

        org = dict()

        for val in t:
            org[val] = 1 + org.get(val, 0)
        
        hmap = dict()

        l=0
        r=0
        min_val = inf
        start, end = -1, -1

        for r, r_val in enumerate(s):

            hmap[r_val] = 1 + hmap.get(r_val, 0)

            while (l <= r and self.isValid(hmap,org)):

                if min_val > r - l + 1:
                    min_val = r - l + 1
                    start, end = l, r + 1

                hmap[s[l]] -= 1
                l += 1

        return s[start : end]
 