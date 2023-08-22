class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float('inf')]*n
        prices[src]=0
        for i in range(k+1):
            tmpPrices=prices.copy()
            for src, d, price in flights:
                if prices[src]==float('inf'): continue
                if prices[src] + price <tmpPrices[d]:
                    tmpPrices[d]=prices[src] + price
            prices=tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]