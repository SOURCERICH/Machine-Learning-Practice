class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.arr = [0] * (n+1)
        self.ptr = 0
    ans = {}
    def insert(self, idKey: int, value: str) -> list[str]:
        self.arr[idKey-1] = value
        ans = []
        while self.arr[self.ptr]:
            ans.append(self.arr[self.ptr])
            self.ptr+=1
        return ans