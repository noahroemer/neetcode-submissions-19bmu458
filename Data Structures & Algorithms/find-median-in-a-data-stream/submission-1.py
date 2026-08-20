class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        self.data.sort()
        length = len(self.data)
        if length % 2 == 0:
            m1 = (length//2)  - 1
            m2 = length//2
            return (self.data[m1] + self.data[m2])/2
        else:
            m = length // 2
            return self.data[m]
            
        
        