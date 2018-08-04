import binaryTrees
import mapanddict
import linkedBinaryTrees

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree"""

    #------------------------- Override Position Class ------------------
    class Position(LinkedBinaryTree.Position)
        def key(self):
            """Return key of map's key-value pair"""
            return self.element()._key

        def value(self):
            """Return value of map's key-value pair"""
            return self.element()._value

    #--------------------- nonpublic utilities --------------------------
    def _subtree_serch(self, p, k):
        """Return Position of p's subtree having key k, or last node searched"""
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_serch(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_serch(self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p"""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return position of last item in subtree rooted at p"""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        """Return the first position in the tree(or None if empty)"""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last position in the tree(or None if empty)"""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the position just before p in the natural order
        Return None if p is the first position"""

        self._validate(p)
        if self.lef(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the position just after p in the natural order
        Return None if p is the last position"""

        self._validate(p)
        if self.lef(p):
            return self._subtree_first_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return position with key k, oe else neighbor (or None if empty)"""
        if self.is_empty():
            return None
        else:
            p = self._subtree_serch(self.root(), k)
            self._rebalance_access(p)
            return p

    def find_min(self):
        """Return (key, value) pair with minimum key (or none if empty)"""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """Return(key, value) pair with least key greater than or equal to k
        Return None if there does not exist such a key"""
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return(p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """Iterate all(key, value) pairs such that start <= key < stop
        If start is NOne, iteration begins with minimum key of map
        If stop is None, iteration continues through the maximum key of map"""

        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # we initialize p with logic similar to find _ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield(p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)"""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_serch(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_serch(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)

    def __iter__(self):
        """Generate an iteration of all keys in the map in order"""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove the item at given Position"""
        self._validate(p)
        if self.last(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
            # now p has at most one child
            parent = self.parent(p)
            self._delete(p)
            self._rebalance_delete(parent)

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)"""
        if not self.is_empty():
            p = self._subtree_serch(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError('Key Error: ' + repr(k))

    def _rebalance_insert(self, p): pass
    def _rebalance_delete(self, p): pass
    def _rebalance_access(self, p): pass

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)"""
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        """Rotate Position p above its parent"""
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root  = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
        # Now rotate x and y, including transfer of middle_subtree
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _restructure(self, x):
        """Perform trinode restructure of positon x with parent/grandparent"""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x


class AVLTreeMap(TreeMap):
    """Sorted map implementation using AVL tree"""

    #------------- nested _Node class ---------------------------------------
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing"""
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0

        def lef_height(self):
            return self._lef_height() if self._left is not None else 0

        def right_height(self):
            return self._right_height() if self._right is not None else 0

    #--------------- positional-based utility methods ---------------------------
    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalanced(self, p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1

    def _tall_child(self, p, favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.last(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.last(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._isbalanced(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.last(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)

    #-------------------- override balancing hooks -------------------------------
    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)


class SplayTreeMap(TreeMap):
    """Sorted map implementation using splay tree"""
    #------------------------- splay operation -------------------------------------
    def _spaly(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                self._rotate(p)
            elif(parent == self.left(grand)) == (p == self.left(parent)):
                self._rotate(p)
                self._rotate(p)

    #---------------------- override balancing hooks ------------------------------
    def _rebalance_insert(self, p):
        self._spaly(p)

    def _rebalance_delete(self, p):
        if p is not None:
            self._spaly(p)

    def _rebalance_access(self, p):
        self._spaly(p)


class RedBlackTreeMap(TreeMap):
    """Sorted map implementation using a red-black tree"""
    class _Node(TreeMap._Node):
        """NOde class for red-black tree maintains bit that denotes color"""
        __slots__ = '_red'

        def __init__(self, element, parent=None, left=None, right=None):
            super.__init__(element, parent, left, right)
            self._red = True

    #-------------- positional-based utility methods -----------------
    def _set_red(self, p):
        p._node._red = True

    def _set_balck(self, p):
        p._node._red = False

    def _set_color(self, p, make_red):
        p._node._red = make_red

    def _is_red(self, p):
        return p is not None and p._node._red

    def _is_red_leaf(self, p):
        return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p):
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None

    #---------------------- support for insertions -------------------------
    def _rebalance_insert(self, p):
        self._resolve_red(p)

    def _resolve_red(self, p):
        if self.is_root(p):
            self._set_balck(p)
        else:
            parent = self.parent(p)
            if self._is_red(parent):
                uncle = self.sibiling(parent)
                if not self._is_red(uncle):
                    middle = self._restructure(p)
                    self._set_balck(middle)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:
                    grand = self.parent(parent)
                    self._set_red(grand)
                    self._set_balck(self.left(grand))
                    self._set_balck(self.right(grand))
                    self._resolve_red(grand)

    #-------------------- support for deletion ------------------------------
    def _rebalance_delete(self, p):
        if len(self) == 1:
            self._set_balck(self.root())
        elif p is not None:
            n = self.num_children(p)
            if n == 1:
                c = next(self.children(p))
                if not self._is_red_leaf(c):
                    self._fix_deficit(p, c)
        elif n == 2:
            if self._is_red_leaf(self.left(p))
                self._set_balck(self.last(p))
            else:
                self._set_balck(self.right(p))

    def _fix_deficit(self, z, y):
        """Resolve balck deficit at z, where y is the root of z's heavier subtree"""
        if not self._is_red(y):
            x = self._get_red_child(y)
            if x is not None:
                old_color = self._is_red(z)
                middle = self._restructure(x)
                self._set_color(middle, old_color)
                self._set_balck(self.left(middle))
                self._set_balck(self.right(middle))
            else:
                self._set_red(y)
                if self._is_red(z):
                    self._set_balck(z)
                elif not self.is_root(z):
                    self._fix_deficit(self.parent(z), self.sibling(z))
        else:
            self._rotate(y)
            self._set_balck(y)
            self._set_red(z)
            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))