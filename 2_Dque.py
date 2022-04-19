from collections import deque


# Array/list implementation of a queue
class ADque:

    def __init__(self):
        self.Adque = deque()

    def is_empty(self):
        return len(self.Adque) == 0

    def push(self, value):
        self.Adque.append(value)

    def peek(self):
        if self.is_empty():
            return "Deque is empty. Nothing to peek at."
        return self.Adque[-1]

    def pop(self):
        if self.is_empty():
            return "Deque is empty. Nothing to pop."
        return self.Adque.pop()


if __name__ == "__main__":
    d = ADque()
    d.push(7)
    d.push(3)
    d.push(8)
    print(f'Last element: {d.Adque[-1]}')
    print(f'Poop: {d.pop()}')
    print(f'Peek: {d.peek()}')
    print(f'Poop: {d.pop()}')
    print(f'Poop: {d.pop()}')
    print(f'Peek: {d.peek()}')
    print(f'Poop: {d.pop()}')

