class QuickFind:
    def __init__(self, size: int()) -> None:
        self.id = [i for i in range(size)]

    def union(self, x: int(), y: int()) -> None:
        if self.id[x] == self.id[y]:
            return
        for i in range(len(self.id)):
            if self.id[i] == self.id[x]:
                self.id[i] = self.id[y]
    
    def connected(self, x: int(), y: int()) -> bool():
        return self.id[x] == self.id[y]