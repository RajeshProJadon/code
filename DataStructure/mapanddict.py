from venv.Lib.operator import itemgetter


class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class"""

    #----------------------- nested _Item calss --------------------------
    class _Item:
        """Lightweight composite to store key-vlaue pairs as map items"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key


class UnsortedTableMap(MapBase):
    """Map implementation using an unsorted list"""

    def __init__(self):
        """create an empty map"""
        self._table = []

    def __getitem__(self, k):
        """Return value associated with key k(raise KeyError if not found)"""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        # did not find match for key
        self._table.append(self._Item(k,v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)"""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map keys"""
        for item in self._table:
            yield  item._key


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression"""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map"""
        self._table = cap * [ None ]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def __resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for(k,v) in old:
            self[k] = v


class ChainHashMap(HashMapBase):
    """Hash map implemented with seperate cahining for collision resolution"""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution"""
    _AVAIL = object()

    def _is_available(self, j):
        """Retrun true if index j is available in table"""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j"""
        firstAvail = None
        while True:
                if self._is_available(j):
                    if firstAvail is None:
                        firstAvail = j
                    if self._table[j] is None:
                        return (False, firstAvail)
                elif k == self._table[j]._key:
                    return (True, j)
                j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j,k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] =  self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key


class SortedTableMap(MapBase):
    """Map implementation using a sorted table"""

    #-------------------- nonpublic behaviors -------------------------
    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k. mod + 1, high)

    #---------------- Public behaviors -----------------------------------
    def __init__(self):
        """Create an empty map"""
        self._table = []

    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwritting existing value if present"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k
            self._table[j]._value = v
        else:
            self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k(raise KeyError if not found)"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum"""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate keys of the map ordered from maximum to minimum"""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """Return(key, value) pair with minimum key(or None if empty)"""
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """Return(key, value) pair with minimum key(or None if empty)"""
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """Return (key, value) pair with least key greater than or equal to k"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        """Return (key, value) pair with greatest key strictly less than k"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j - 1]._key, self._table[j - 1]._value)
        else:
            return None

    def find_gt(self, k):
        """Return (key, value) pair with least key strictly greater then k"""
        j == self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None


    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop"""
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield(self._table[j]._key, self._table[j]._value)
            j += 1