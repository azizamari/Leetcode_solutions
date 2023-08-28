class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res=[]
        cur=products
        for i in range(len(searchWord)):
            res.append([])
            for x in cur:
                if i<len(x) and x[i]==searchWord[i]: res[-1].append(x)
            cur=res[-1]
        return [x[:3] for x in res]

