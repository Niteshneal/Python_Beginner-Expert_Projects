class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        min = 101
        max = 0
        for e in self.__elements:
            if e < min:
                min = e
            if e > max:
                max = e
        self.maximumDifference = max - min


_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
