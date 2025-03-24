# 對一個未排序的list求中間值，且會持續加新的item到list中。
# 若先排序，O(nlogn)，求中間值 O(1)，但若加新的item到list中，每加入一個item時需要將其插入以排序的list中 O(n)，加入 m 個item為 O(m * n)
# 用兩個heap，插入為 O(logn)，求中間值 O(1)
import heapq

class Median:
    def __init__(self):
        # self.small is a maxheap
        # self.big is a minheap
        self.small, self.big = [], []
    
    def insert(self, val: int) -> None:
        heapq.heappush(self.small, -1 * val)
        
        if self.big and self.big[0] <= val: # 確保 small 的值小於 big的值
            heapq.heappop(self.small)
            heapq.heappush(self.big, val)

        if len(self.small) > len(self.big) + 1: # small 與 big 的數量差值必須 <= 1
            item = -1 * heapq.heappop(self.small)
            heapq.heappush(self.big, item)
        
        elif len(self.big) > len(self.small) + 1: # small 與 big 的數量差值必須 <= 1
            item = heapq.heappop(self.big)
            heapq.heappush(self.small, -1 * item) # 插入small (maxheap) 前須先將值 * -1


    def getMedian(self):
        if len(self.small) > len(self.big):
            print(f"median is {-1 * self.small[0]}")
            return -1 * self.small[0]
        elif len(self.big) > len(self.small):
            print(f"median is {self.big[0]}")
            return self.big[0]
        else:
            print(f"median is {(-1 * self.small[0] + self.big[0]) / 2}")
            return (-1 * self.small[0] + self.big[0]) / 2
    
    def showHeap(self):
        print(f"small : {self.small}")
        print(f"big : {self.big}")

nums = [4,7,3,9,5,1,10]
test = Median()
for i in nums:
    test.insert(i)
    test.getMedian()

test.insert(11)
test.getMedian()
test.showHeap()