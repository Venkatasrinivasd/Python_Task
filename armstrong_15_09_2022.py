n = int(input("enter number of armstrong numbers: "))
lst1 = []
for i in range(n):
    num = i
    count = 0
    r = len(str(i))
    while i != 0:
        k = i % 10
        count = count + k ** r
        i = i // 10
    if num == count:
        lst1.append(count)
print(lst1[9])
