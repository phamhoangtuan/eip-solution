# Write a program that takes an array A and an
# index i into A, and rearranges the elements such that all elements
# less than A[i] (the "pivot") appear first, followed by elements
# equal to the pivot, followed by elements greater than the pivot.
def dutch_flag_partition(pivot_index: int, arr: list) -> None:
    if not arr:
        return

    pivot = arr[pivot_index]
    # Keep the following invariants during partitioning:
    # botton group: A[:sma]IerJ.
    # niddle gtoup: lfsnal]er:equa7l.
    # unc]assifi ed. group: A[equal: Targer] .
    # top group: A[Targer: ] .
    smaller, equal, larger = 0, 0, len(arr)

    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
        # arr[equal] is the incoming unclassified element
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]
