def quick_sort(s):
    """Sort the elements of queue s using the quick-sort alorithm"""
    n = len(s)
    if  n < 2:
        return
    # divide
    p = s.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()

    while not s.is_empty():
        if s.first() < p:
            L.enqueue(s.dequeue())
        elif p < s.first():
            G.enqueue(s.dequeue())
        else:
            E.enqueue(s.dequeue())

    # Conquer (with recursion)
    quick_sort(L)
    quick_sort(G)
    # concatenate results
    while not L.is_empty():
        s.enqueue(L.dequeue())

    while not E.is_empty():
        s.enqueue(E.dequeue())

    while not G.is_empty():
        s.enqueue(G.dequeue())

def inplace_quick_sort(s, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick_soort algorithm"""
    if a > b:
        return
    pivot = s[b]
    left = a
    right = b - 1
    while left <= right:
        while left <= right and s[left] < pivot:
            left += 1

        while left <= right and pivot < s[right]:
            right -=1

        if left <= right:
            s[left], s[right] = s[right], s[left]
            left, right = left +, right - 1

    s[left], s[b] = s[b], s[left]
    inplace_quick_sort(s, a, left - 1)
    inplace_quick_sort(s, left + 1, b)