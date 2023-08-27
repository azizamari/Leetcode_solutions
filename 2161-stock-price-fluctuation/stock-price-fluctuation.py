class StockPrice:

    def __init__(self):
        self.hash={}
        self.minh=[]
        self.maxh=[]
        self.last=0
        

    def update(self, timestamp: int, price: int) -> None:
        self.hash[timestamp]=price
        if self.last<=timestamp: self.last=timestamp
        heappush(self.maxh, (-price,timestamp))
        heappush(self.minh, (price,timestamp))

    def current(self) -> int:return self.hash[self.last]
    def maximum(self) -> int:
        # clean up residue maxes
        while self.hash[self.maxh[0][1]]!=-self.maxh[0][0]:heappop(self.maxh)
        return -self.maxh[0][0]

    def minimum(self) -> int:
        # clean up residue mins
        while self.hash[self.minh[0][1]]!=self.minh[0][0]:heappop(self.minh)
        return self.minh[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()