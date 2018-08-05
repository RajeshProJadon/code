def merge(s1, s2, s):
    """Merge two sorted Python lists S1 and S2 into properly sizez list S."""

    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1

def merge_sort(s):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(s)
    if n < 2:
        return
    # divide
    mid = n//2
    s1 = s[0:mid]
    s2 = s[mid:n]
    # conquer (with recursion)
    merge_sort(s1)
    merge_sort(s2)
    # merge results
    merge(s1, s2, s)
