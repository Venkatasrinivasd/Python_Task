lst1 = [14, 9, 57, 12, 23, 44, 7]
'''Bubble sort algorithm 
[9, 14, 57, 12, 23, 44, 7]
[9, 14, 12, 57, 23, 44, 7]
[9, 14, 12, 23, 57, 44, 7]
[9, 14, 12, 23, 44, 57, 7]
[9, 14, 12, 23, 44, 7, 57] 1 st iteration
[9, 12, 14, 23, 44, 7, 57]
[9, 12, 14, 23, 7, 44, 57] 2 nd iteration
[9, 12, 14, 7, 23, 44, 57] 3 rd iteration
[9, 12, 7, 14, 23, 44, 57] 4 th iteration
[9, 7, 12, 14, 23, 44, 57] 5 th iteration
[7, 9, 12, 14, 23, 44, 57] 6 th iteration
bubble sort algorithm check one by one and swap

 '''
for j in range(len(lst1)-1):
    for i in range(len(lst1)-1):
        if lst1[i] > lst1[i+1]:  # comparing by using indexing
            lst1[i], lst1[i+1] = lst1[i+1], lst1[i]  # sorting the elements
print(lst1)  # printing list from low to high
lst1 = [14, 9, 57, 12, 23, 44]
for j in range(len(lst1)-1):
    for i in range(len(lst1)-1):
        if lst1[i] < lst1[i+1]:
            lst1[i], lst1[i+1] = lst1[i+1], lst1[i]
print(lst1)  # printing list from high to low
