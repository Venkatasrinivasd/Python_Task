def shell_sort(lst2):
    gap = len(lst2)//2
    while gap > 0:
        for index in range(gap, len(lst1)):
            curr_element = lst2[index]
            pos = index
            while pos >= gap and curr_element < lst2[pos - gap]:
                lst2[pos] = lst2[pos - gap]
                pos = pos - gap
            lst2[pos] = curr_element
        gap = gap//2


lst_len = int(input("list length : "))
lst1 = [int(input()) for i in range(lst_len)]
shell_sort(lst1)
print("sorted list: ", lst1)
