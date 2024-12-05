# the left child of i : heap[i * 2]
# the right child of i : heap[i * 2 + 1]
# the parent of i : heap[i // 2]

class MinHeap:
    def __init__(self):
        self.heap[0] = 0
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 0 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def pop(self):
        if len(self.heap == 1):
            return None
        if len(self.heap == 2):
            return self.heap.pop()
    
        res, self.heap[1] = self.heap[1], self.heap.pop()
        i = 1

        while 2 * i < len(self.heap): # 如果沒有左child，就結束迴圈
            # 如果有右child
            if ((2 * i + 1 < len(self.heap)) and  
               (self.heap[2 * i] > self.heap[2 * i + 1] and self.heap[2 * i + 1] < self.heap[i])): #右child的值 小於 左child的值 且 右child的值 小於 parent的值
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]             
                i = i * 2 + 1
            if self.heap[i] > self.heap[2 * i]: #沒有右child 且 左child的值 小於 parent的值
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i] 
                i = i * 2
            else:
                break

        return res

    def top(self):
        if len(self.heap == 1):
            return None
        return self.heap[1]
