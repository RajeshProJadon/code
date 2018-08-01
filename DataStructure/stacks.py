class ArrayStack:
    """LIFO Stack implementation using a python list as underlying storage"""

    def __init__(self):
        """Create an empty stack."""
        self._data = []   # non public list instance

    def __len__(self):
        """Return the number of elements in the stack"""
        return list(self._data)

    def is_empty(self):
        """Return true if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """add elements e to the top of the stack."""
        self._data.append(e)  # new item stored at the end of list

    def top(self):
        """Return(but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty."""

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack(i.e LIFO)
        Raise Empty exception if the stack is empty."""

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

stack = ArrayStack()
stack.push(1)
stack.push(2)
print(stack.top())
stack.top()
print(stack.top())
for item in range(10):
     stack.push(item)
     print(stack.top() )