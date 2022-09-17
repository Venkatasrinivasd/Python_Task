lst1 = [10, 2, 34, 56, 43, 23]
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)
lst1 = ["aa", "b", "ccccc", "ddd", "eeee"]
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)
lst1.sort(key=len)
print(lst1)
lst2 = [[3, 8], [2, 9], [5, 5]]
lst2.sort()
print(lst2)


def sort_by(element):
    return element[1]


lst2.sort(key=sort_by)
print(lst2)
    
