class Stack:
    def __init__(self):
      self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
          return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
stack=Stack()
stack.push("Apple")
stack.push("Banna")
stack.push("Cherry")
print("The size of stack is :",stack.size())
print("Is stack empty?",stack.is_empty())
print("Top item on the stack :",stack.peek())
print("Popped item:",stack.pop())
print("Popped item:",stack.pop())
print("Popped item:",stack.pop())
print("Is stack empty?",stack.is_empty())
print("The size of stack is :",stack.size())
