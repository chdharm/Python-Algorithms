"""MaxHeap implementation using python"""


class MaxHeap(object):

	def __init__(self, maxSize=None):
		self.heap = []
		self.HEAP_SIZE = maxSize

	def _swap(self,i,j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def _heapIsFull(self):
		return (self.HEAP_SIZE != None and len(self.heap) >= self.HEAP_SIZE)

	def insert(self, item):
		if self._heapIsFull():
			"Heap is full..."
		else:
			self.heap.append(item)
			# adjust parent node item
			self._bubbleUp(len(self.heap)-1)

	def _bubbleUp(self, currentPosition):
		if currentPosition >= 1: # no need to do bubbleUp for 1 element
			index = currentPosition
			parentIndex = (index-1)//2

			if parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
				self._swap(parentIndex, index)
				self._bubbleUp(parentIndex)
			
	def peek(self):
		return self.heap[0] if self.heap else None

	def pop(self):
		element = self.peek()
		if element:
			self._swap(0, len(self.heap) - 1) # swap first element to last element
			self.heap.pop()
			self._bubbleDown(0)
		return element

	def _bubbleDown(self, index):
		leftChildIndex = 2 * index + 1 
		rightChildIndex = 2 * index + 2
		largest = index
		if len(self.heap) > leftChildIndex and self.heap[largest] < self.heap[leftChildIndex]:
			largest = leftChildIndex
		if len(self.heap) > rightChildIndex and self.heap[largest] < self.heap[rightChildIndex]:
			largest = rightChildIndex
		if largest!=index:
			self._swap(index, largest)
			self._bubbleDown(largest)
