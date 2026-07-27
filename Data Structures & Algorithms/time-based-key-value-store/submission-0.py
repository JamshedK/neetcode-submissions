class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap: 
            self.hashmap[key].append([value, timestamp])
        else:
            self.hashmap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        # do a binary search
        if key not in self.hashmap:
            return ''
        array = self.hashmap[key]
        l, r = 0, len(array) - 1
        prev = ''
        while l <= r: 
            mid = (l + r) // 2
            mid_timestamp = array[mid][1]
            if mid_timestamp == timestamp:
                return array[mid][0]
            # if mid timestamp is smaller that timestamp
            if mid_timestamp < timestamp:
                prev = array[mid][0]
                l = mid + 1
            # if mid timestamp is greater
            else: # timestamp > mid_timestamp
                r = mid - 1
        return prev
