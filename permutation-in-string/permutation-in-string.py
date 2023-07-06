class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars=defaultdict(int)
        for i in range(len(s1)):
            chars[s1[i]] += 1
    
        def first_occ(s2,indice):
            while indice<len(s2):
                if s2[indice] in chars:
                    return indice
                indice+=1
            return -1
        indice=first_occ(s2, 0)
        while indice!=-1:
            curr=defaultdict(int)
            potential=True
            newindice=indice+1
            if indice+len(s1)>len(s2): break
            for i in range(indice,indice+len(s1)):
                if s2[i] not in chars:
                    potential=False
                    newindice=i+1
                    break
                else:
                    curr[s2[i]]+=1
            if potential:
                istrue=True
                for key in chars.keys():
                    if chars[key] != curr[key]:
                        istrue=False
                        break
                if istrue: return True
            indice=first_occ(s2,newindice)
        return False
                        
                