class LinkedListStack:
    """LIFO stack implementation using a singly linked list for storage"""

    #-------------------------Nested _Node Class-----------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked list node"""
        __slots__ = '_element', '_next'     # streamline memory usage

        def __init__(self, element, next):
            self._element =  element
            self._next = next

    #------------------------Stack Methods-----------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None                 # Reference to the head node
        self._size = 0                    # Number of stack elements

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return true if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)   # Create and link a new node
        self._size += 1

    def top(self):
        """Return the element at the top of the stack
        Raise Empty exception if the stack is empty"""

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack(i.e LIFO)
        Raise Empty execption if the stack is empty"""

        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next      # byepass the former top node
        self._size -=
        return answer
