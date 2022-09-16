def ins_sort(lt1):
    for index in range(1, len(lt1)):
        current_element = lt1[index]
        pos = index
        while current_element < lt1[pos-1] and pos > 0:
            lt1[pos] = lt1[pos - 1]
            pos = pos - 1
            lt1[pos] = current_element


lss = [15, 17, 4, 13, 2, 44]
ins_sort(lss)
print(lss)
