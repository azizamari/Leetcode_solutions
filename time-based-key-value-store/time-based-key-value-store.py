class TimeMap:

    def __init__(self):
        self.timestamps={}    
        self.history_timestamps={}    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[str(timestamp)+'#'+key]=value
        if key in self.history_timestamps:
            self.history_timestamps[key].append(timestamp)
        else: self.history_timestamps[key]=[timestamp]
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result
    def get(self, key: str, timestamp: int) -> str:
        if str(timestamp)+'#'+key in self.timestamps:
            return self.timestamps[str(timestamp)+'#'+key]
        else: 
            if not key in self.history_timestamps: return ""
            arr=self.history_timestamps[key]
            x=self.binary_search(arr,timestamp)
            if x!=-1:
                return self.timestamps[str(arr[x])+'#'+key]
            else: return "" 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)