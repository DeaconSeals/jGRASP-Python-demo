class ArrayQueue:
   def __init__(self, capacity=1):
      self.elements = [None for _ in range(capacity)]
      self.front = 0
      self.rear = 0
      self.size = 0
   
   def resize(self, capacity=1):
      temp = [None for _ in range(capacity)]
      j = self.front
      for i in range(self.size):
         temp[i] = self.elements[j]
         j = (j + 1) % len(self.elements)
      self.elements = temp
      self.front = 0
      self.rear = self.size
   
   def size(self):
      return self.size
      
   def is_empty(self):
      return self.size == 0
   
   def enqueue(self, element):
      if self.size == len(self.elements):
         self.resize(len(self.elements)*2)
      self.elements[self.rear] = element
      self.rear = (self.rear + 1) % len(self.elements)
      self.size += 1

   def dequeue(self):
      if self.is_empty():
         return None
      result = self.elements[self.front]
      self.elements[self.front] = None
      self.front = (self.front + 1) % len(self.elements)
      self.size -= 1
      return result

   def first(self):
      if self.is_empty():
         return None
      return self.elements[self.front]

if __name__ == '__main__':
   queue1 = ArrayQueue(6)
   queue1.enqueue('A')
   queue1.enqueue('B')
   queue1.enqueue('C')
   queue1.enqueue('D')
   queue1.dequeue()
   queue1.dequeue()
   queue1.dequeue()
   queue1.enqueue('E')
   queue1.enqueue('F')
   queue1.enqueue('G')
   queue1.enqueue('H')

   queue2 = ArrayQueue(3)
   queue2.enqueue('A')
   queue2.enqueue('B')
   queue2.enqueue('C')
   queue2.dequeue()
   queue2.dequeue()
   queue2.enqueue('D')
   queue2.enqueue('E')
   queue2.enqueue('F')