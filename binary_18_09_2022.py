def binary_search(lst1, key):
    low = 0
    high = len(lst1)-1
    fnd = False
    while low <= high and not fnd:
        mid = (low + high) // 2
        if key == lst1[mid]:
            fnd = True
        elif key > lst1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if fnd:
        print("key is found ")
    else:
        print("not found")


lt1 = [23, 53, 67, 27, 14, 62]
lt1.sort()
print(lt1)
key1 = int(input("enter the key value: "))
binary_search(lt1, key1)

