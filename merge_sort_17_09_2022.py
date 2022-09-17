def merge_sort(lst1):
    if len(lst1) > 1:
        mid = len(lst1) // 2
        left_lst = lst1[:mid]
        right_lst = lst1[mid:]
        merge_sort(left_lst)
        merge_sort(right_lst)
        i = 0
        j = 0
        k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst1[k] = left_lst[i]
            else:
                lst1[k] = right_lst[j]


num = int(input("how many elements you want in list: "))
lst1 = [int(input()) for x in range(num)]
