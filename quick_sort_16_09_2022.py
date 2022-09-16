def pivot_place(lt1, first, last):
    pivot = lt1[first]
    left = first + 1
    right = last
    while True:
        while left <= right and lt1[left] <= pivot:
            left = left + 1
        while left <= right and lt1[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            lt1[left], lt1[right] = lt1[right], lt1[left]
    lt1[first], lt1[right] = lt1[right], lt1[first]
    return right


def q_sort(list1, first, last):
    if first < last:
        p = pivot_place(list1, first, last)
        q_sort(list1, first, p-1)
        q_sort(list1, p+1, last)


lst1 = [56, 26, 93, 17, 31, 44]
n = len(lst1)
q_sort(lst1, 0, n-1)
print(lst1)
