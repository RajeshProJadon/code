class _DoublyLinkedBase:
    """A base class providing a doubly linked list representations"""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return true if the list is empty"""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)  # linked to neighbours
        prdecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element"""
        predecessor = node._prev
        successor = node._next
        prdeccessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class LinkedDeque(_DoublyLinkedBase):
    """Double ended queue implementation based on a doubly linked list"""

    def first(self):
        """Return(but do not remove ) the element at the front of the dequeue"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        """Return(but do not remove ) the element at the back of the dequeue"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add an element to the back of the deque"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the fron of the deque
        Raise Empty exception if the deque is empty"""
        if self.is_empty():
            raise Empty("Dewue is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque
        Raise Empty exception if the deque is empty"""

        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access"""

    #--------------------Nested position class-------------------------
    class position:
        """An abstraction representing the location of a single element"""

        def __init__(self):
            """Construtor should not be invoke by user"""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at the position"""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not(self == other)

    #----------------------Utility method---------------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return position instance for given node(or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    #----------------------Accessors---------------------------------------
    def first(self):
        """Return the first position in the list(or none if list is empty)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last position in the list(or none if list is empty)"""
        return self._make_position(self._header._prev)

    def before(self, p):
        """Return the position just before position p(or none if p is first)"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the position just after position p(or none if p is last)"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element
            cursor = self.after(cursor)

    #------------------------mutators-------------------------------------------
    # override inherited version to return position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new position"""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new position"""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new position"""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before position p and return new position"""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after position p and return new position"""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at position p"""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at position p with e
        return the element formerly at position p"""

        original = self._validate(p)
        plo_value = original._element
        original._element = e
        return old_value

    def insertion_sort(L):
        """Sort positionalList of comparable elements into nondecreasing order"""
        if len(L) > 1:
            marker = L.first()
            while marker != L.last():
                pivot = L.after(marker)
                value = pivot.element()
                if value > marker.element():
                    marker = pivot
                else:
                    walk = marker
                    while walk != L.first() and L.before(walk).element() > value:
                        walk = L.before(walk)
                    L.delete(pivot)
                    L.add_before(walk, value)


class FavoritesList:
    """List of elements ordered from most frequently accessed to least"""

    #--------------------- nested _Item class----------------------------
    class _Item:
        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e
            self._count = 0

    #------------------- nonpublic utilities ----------------------------
    def _find_position(self, e):
        """Search for element e and return its position (or None if not found)"""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at position p earlier in the list based on access count"""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while(walk != self._data.first() and
                      cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    #---------------- public methods -------------------------------------
    def __init__(self):
        """Create an empty list of favorites"""
        self._data = PositionalList()

    def __len__(self):
        """Return number of entries on favorites list"""
        return len(self._data)

    def is_empty(self):
        """Return true if list is empty"""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count"""
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """Remove element e from the list of favorites"""
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if not 1 <= K <= len(self):
            raise ValueError('Illegal value for K')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)