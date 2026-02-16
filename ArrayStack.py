class ArrayStack:
   def __init__(self, capacity=1):
      self.elements = [None for _ in range(capacity)]
      self.top = 0
   
   def resize(self, capacity):
      temp = [None for _ in range(capacity)]
      for i in range(self.top):
         temp[i] = self.elements[i]
      self.elements = temp
   
   def size(self):
      return self.top
      
   def is_empty(self):
      return self.size()==0
   
   def push(self, element):
      if self.size() == len(self.elements):
         self.resize(len(self.elements)*2)
      self.elements[self.top] = element
      self.top += 1
   
   def pop(self):
      if self.is_empty():
         return None
      self.top -= 1
      top_value = self.elements[self.top]
      self.elements[self.top] = None
      if self.top > 0 and self.top < len(self.elements)//4:
         self.resize(len(self.elements//2))
      return top_value
   
   def peek(self):
      if self.is_empty():
         return None
      return self.elements[self.top-1]

if __name__ == '__main__':
   stack = ArrayStack()
   stack.push('A')
   stack.push('B')
   stack.push('C')
   stack.pop()