from builtins import set


class Tree:
    """Abstract base class representing a tree structure"""

    #---------------------- nested position class --------------
    class Position:
        """an abstraction representing the location of a single element"""

        def element(self):
            """Return the element stored at this position"""
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            """Return true if other position represents the same location"""
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            """Return true if other does not represent the same location"""
            return not (self == other)

    #------------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return position representing the trees root(or None if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return position representing p's parent(or None of p is root)"""
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        """Return the number of children that position p has"""
        raise NotImplementedError('Must be implementd by subclass')

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError('Must be implemented by subclass')

    #-------------- concrete methods implemented in this class ------------------
    def is_root(self):
        """Return True if Position p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if position p does not jhave any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return true if the tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """Return the number if levels separating position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of the tree"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Return the height of subtree rooted at position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at position p
        IF p i None, returnthe height of the entire tree"""

        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        """Generate an iteration of the tree's elements"""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of postitions in the trees"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of postitions in subtree rooted at p"""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def positions(self):
        """Generate an iteration of the tree's positions"""
        return self.preorder()

    def postorder(self):
        """Generate a postorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in sunbtree rooted at p"""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        """Generate a breadth-first iteration of the position of the tree"""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.denqueue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)