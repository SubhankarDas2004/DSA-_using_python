def partition(a, l, r):
    pivot = a[l]   # pivot element
    left = l + 1
    right = r

    while True:
        # move left pointer
        while left <= right and a[left] <= pivot:
            left += 1

        # move right pointer
        while left <= right and a[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            a[left], a[right] = a[right], a[left]

    # place pivot in correct position
    a[l], a[right] = a[right], a[l]
    return right


def quick_sort(a, l, r):
    if l < r:
        p = partition(a, l, r)
        quick_sort(a, l, p - 1)
        quick_sort(a, p + 1, r)


# Example
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
