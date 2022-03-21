
class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        print(self.stack[-1])

    def pop(self):
        if self.is_empty():
            return "Stack is empty. Nothing to pop."
        self.stack.pop()

    def push(self, value):
        self.stack.append(value)


if __name__ == "__main__":

    s = Stack()
    s.push(5)
    s.push(7)
    s.peek()
    s.pop()
    s.peek()
    s.pop()
    print(s.pop())
    print(s.is_empty())

