class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.top = Node(element, self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        top_value = self.top.element
        self.top = self.top.next
        self.size -= 1
        return top_value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.element


class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next = next_node

if __name__ == '__main__':
    stack = LinkedStack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    stack.pop()