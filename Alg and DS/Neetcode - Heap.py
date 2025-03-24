# the left child of i : heap[i * 2]
# the right child of i : heap[i * 2 + 1]
# the parent of i : heap[i // 2]

class MinHeap:
    def __init__(self):
        self.heap[0] = 0
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # percolate up
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

        # percolate down
        while 2 * i < len(self.heap): # 如果沒有左child，就結束迴圈
            # 如果有右child
            if ((2 * i + 1 < len(self.heap)) and  
               (self.heap[2 * i] > self.heap[2 * i + 1] and self.heap[2 * i + 1] < self.heap[i])): #右child的值 小於 左child的值 且 右child的值 小於 parent的值
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]             
                i = i * 2 + 1
            elif self.heap[i] > self.heap[2 * i]: #沒有右child 且 左child的值 小於 parent的值
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i] 
                i = i * 2
            else:
                break

        return res

    def top(self):
        if len(self.heap == 1):
            return None
        return self.heap[1]
    
    def heapify(self,arr):
        # move the 0th val to the arr end 
        arr.append(arr[0])
        self.heap = arr

        cur = (len(self.heap) - 1) // 2

        while cur > 0:
            i = cur
            while i * 2 < len(self.heap):
                if self.heap[i * 2 + 1] < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i] < self.heap[i * 2 + 1]:
                    self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                    i = i * 2 + 1
                elif self.heap[i] < self.heap[i * 2]:
                    self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                    i = i * 2
                else:
                    break
            cur -= 1





