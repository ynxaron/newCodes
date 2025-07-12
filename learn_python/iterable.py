class StrangeName:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        inx = self.index
        if inx < len(self.firstName) and inx < len(self.lastName):
            self.index += 1
            return f"{self.firstName[inx]}-{self.lastName[inx]}"
        raise StopIteration

sn = StrangeName("Satyam", "Prakash")
sn = iter(sn)
print(next(sn))
print(next(sn))
print(next(sn))
print(next(sn))
print(next(sn))
print(next(sn))
print(next(sn))
