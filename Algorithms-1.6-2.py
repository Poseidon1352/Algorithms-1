def parent(i):
    return int((i-1)/2)
def left(i):
    return i*2 + 1
def right(i):
    return i*2 + 2
    
class Heap:
    def __init__(self,type_):
        self.type_ = type_
        self.arr = []
        self.size = 0
    
    def swap_nodes(self,i,j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp
        
    def bubble_down(self,i):
        l = left(i)
        r = right(i)
        swap_loc = i
        if l < self.size:
            if self.type_ == 'min' and self.arr[swap_loc] > self.arr[l]:
                swap_loc = l
            elif self.type_ == 'max' and self.arr[swap_loc] < self.arr[l]:
                swap_loc = l
        if r < self.size:
            if self.type_ == 'min' and self.arr[swap_loc] > self.arr[r]:
                swap_loc = r
            elif self.type_ == 'max' and self.arr[swap_loc] < self.arr[r]:
                swap_loc = r
        if swap_loc != i:
            self.swap_nodes(i,swap_loc)
            self.bubble_down(swap_loc)
                       
    def extract_top(self):
        top = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size = self.size - 1
        self.bubble_down(0)
        self.arr.pop()
        return top
    
    def insert(self,val):
        i = self.size
        self.size = self.size + 1
        self.arr.append(val)
        if self.type_ == 'min':
            while i > 0 and self.arr[parent(i)] > self.arr[i]:
                self.swap_nodes(i,parent(i))
                i = parent(i)
        else:
            while i > 0 and self.arr[parent(i)] < self.arr[i]:
                self.swap_nodes(i,parent(i))
                i = parent(i)

                
maxHeap = Heap('max')
minHeap = Heap('min')
file = open('Median.txt','r')
median_sum = 0
for v in range(0,10000):
    num = int(file.readline().split()[0])
    
    if v == 0:
        median = num
        prev = num
    elif v == 1:
        if prev > num:
            minHeap.insert(prev)
            maxHeap.insert(num)
        elif num > prev:
            minHeap.insert(num)
            maxHeap.insert(prev)
        median = maxHeap.arr[0]
    else:
        if num < minHeap.arr[0] and num > maxHeap.arr[0]:
            if minHeap.size >= maxHeap.size:
                maxHeap.insert(num)
            else:
                minHeap.insert(num)
        elif num < maxHeap.arr[0]:
            if minHeap.size >= maxHeap.size:
                maxHeap.insert(num)
            else:
                temp = maxHeap.extract_top()
                minHeap.insert(temp)
                maxHeap.insert(num)
        else:
            if maxHeap.size >= minHeap.size:
                minHeap.insert(num)
            else:
                temp = minHeap.extract_top()
                maxHeap.insert(temp)
                minHeap.insert(num)
                
        if maxHeap.size < minHeap.size:
            median = minHeap.arr[0]
        else:
            median = maxHeap.arr[0] 
               
    median_sum = (median + median_sum)

print(median_sum%10000)