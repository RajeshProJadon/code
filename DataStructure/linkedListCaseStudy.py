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