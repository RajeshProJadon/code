from favoritesLinkedListMTF import highPos


class FavoritesListMTF:
    """List of elements ordered with move-to-front heuristic"""

    # we override _move_up to provide movre-to-front semantics
    def _move_up(self):
        """MOve accessed item at position p to front list"""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))     # delete/reinsert

   # we override top because list is no longer sorted
   def top(self, k):
       """Generate sequence of top k elements interms of access count"""
       if not 1 <= k <= len(self):
           raise ValueError('Illegal value for k')

    # we begin by making a copy of the orirginal list
    temp = PositionalList()
    for item in self._data:
        temp.add_last(item)

    # we repeatedly find, report, and remove element with largest count
    for j in range(k):
        # find and report next highest from temp
        highPos = temp.first()
        walk = temp.after(highPos)
        while walk is not None:
            if walk.element()._count > highPos.element()._count:
                highPos = walk
            walk = temp.after(walk)
        # We have found the element with higest count
        yield highPos.element()._value
        temp.delete(highPos)