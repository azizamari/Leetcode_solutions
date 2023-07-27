from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.srt = SortedList()

    def addNum(self, num: int) -> None:
        self.srt.add(num)

    def findMedian(self) -> float:
        return median(self.srt)