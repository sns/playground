from typing import List
from enum import Enum

class HeapType(Enum):
    MinHeap = 0
    MaxHeap = 1 

class BinaryHeap:
    def __init__(self, inputList: List[int] = [], heapType: HeapType = HeapType.MinHeap):
       self._list = inputList
       self._heapType = heapType
    
    def getHeapType(self):
        return self._heapType

    def getSize(self):
        return len(self._list)

    def print(self):
        print(self._list)
    
    def getParentIndex(self, childIndex: int) -> int:
        pIndex = (childIndex-2)/2 if childIndex % 2 == 0 else (childIndex - 1)/2
        if not (-1 < pIndex < self.getSize()):
            # raise ValueError("Index out of range: invalid parent index")
            return None
        return pIndex

    def push(self, item: int) -> None:
        self._list.insert(0, item)
        self.heapify(0)
    
    def pop(self) -> int:
        if self.getSize() == 0:
            return None
        self._swap(0, self.getSize()-1)
        ret = self._list.pop()
        self.heapify(0)       
        return ret

    def _isValidIndex(self, index: int):
        return -1 < index < self.getSize()

    def peek(self, index: int) -> int:
        return self._list[index] if self._isValidIndex(index) else None

    def _isMaxHeap(self) -> bool:
        return self.getHeapType() == HeapType.MaxHeap
    
    def _swap(self, i1: int, i2: int) -> None:
        self._list[i1], self._list[i2] = self._list[i2], self._list[i1]

    def heapify(self, index: int) -> None:
        if not self._isValidIndex(index):
            return
        p = self.peek(index)
        lIndex = 2*index+1
        rIndex = 2*index + 2
        self.heapify(lIndex)
        self.heapify(rIndex)
        l = self.peek(lIndex) 
        r = self.peek(rIndex)
        if l is None and r is None:
            return
        if self._isMaxHeap():
            m = p
            if l is not None and r is not None:
                m = max(p, l, r)
            elif l is None:
                m = max(p, r)
            else:
                m = max(p, l)
            if m == p:
                return
            elif m == l:
                self._swap(index,  lIndex)
                self.heapify(lIndex)
            elif m == r:
                self._swap(index,  rIndex)
                self.heapify(rIndex)
        else:
            m = p
            if l is not None and r is not None:
                m = min(p, l, r)
            elif l is None:
                m = min(p, r)
            else:
                m = min(p, l)
            
            if m == p:
                return
            
            elif m == l:
                self._swap(index,  lIndex)
                self.heapify(lIndex)
            elif m == r :
                self._swap(index,  rIndex)
                self.heapify(rIndex)                           
# minHeap = BinaryHeap([2,6,3,7,5,8,19,23,44,33,11,1, 10])
minHeap = BinaryHeap([2,6,3,1])
minHeap.print()
minHeap.heapify(0)
minHeap.print()
print(minHeap.pop())
minHeap.print()
minHeap.push(4)
minHeap.print()

print("*******************************")
import heapq
l = [2,6,3,1]
print(l)
heapq.heapify(l)
print(l)
print(heapq.heappop(l))
print(l)
heapq.heappush(l, 4)
print(l)

print("*******************************")
myList = [2,6,3,7,5,8,19,23,44,33,11,1, 10]
myMaxHeap = BinaryHeap(myList[:], HeapType.MaxHeap)
myMinHeap = BinaryHeap(myList[:], HeapType.MinHeap)
myMaxHeap.heapify(0)
myMinHeap.heapify(0)
sortedAsc=[]
sortedDesc=[]
while myMaxHeap.peek(0) is not None:
    sortedAsc.append(myMaxHeap.pop())
while myMinHeap.peek(0) is not None:
    sortedDesc.append(myMinHeap.pop())
print(myList)
print(sortedAsc)
print(sortedDesc)