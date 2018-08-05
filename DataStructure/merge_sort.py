def merge(s1, s2, s):
    """Merge two sorted queue instances s1 and s2 into empty queue s."""
    while not s1.is_empty() and not s2.is_empty():
        if s1.first() < s2.first():
            s.enqueue(s1.dequeue())
        else:
            s.enqueue(s2.dequeue())

    while not s1.is_empty():
        s.enqueue(s1.dequeue())

    while not s2.is_empty():
        s.enqueue(s2.dequeue())

def merge_sort(s):
    """SOrt the elements of queue s using the merge-sort algorithm"""
    n = len(s)
    if n < 2:
        return
    # divide
    s1 = LinkedQueue()
    s2 = LinkedQueue()

    while len(s1) < n //2:
        s1.enqueue(s.dequeue())

    while not s.is_empty():
        s2.enqueue(s.dequeue())
    # Conquer (with recursion)
    merge_sort(s1)
    merge_sort(s2)
    # merge results
    merge(s1, s2, s)