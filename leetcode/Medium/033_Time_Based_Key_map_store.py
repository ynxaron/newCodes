class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, time: int):
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([time, value])

    def get(self, key: str, time: int) -> str:
        res = ""
        arr = self.map.get(key, [])
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= time:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

def implementing_timebase(ins: list[str], data: list[list[str]]) -> list[str | None]:
    res = []
    timemap = None
    for i in range(len(ins)):
        ans = None
        if ins[i] == "TimeMap":
            timemap = TimeMap()
        if timemap is not None:
            if ins[i] == "set":
                key, value, time = data[i]
                timemap.set(key, value, int(time))
            if ins[i] == "get":
                key, time = data[i]
                ans = timemap.get(key, int(time))
        res.append(ans)
    return res
