# reverse the list using for loop
lis1 = [10, 18, 15, "venkat", 6.7, 10]
lis2 = []
for i in range(len(lis1)-1, -1, -1):
    lis2.append(lis1[i])
print(lis2)
lis1 = [10, 18, 15, 17, 60]
print(lis1[::-1])
str1 = "hi how are u"
print(str1[::-1])

n = input("enter any number: ")

if n == n[::-1]:
    print("given number is palindrome")
else:
    print("not a palindrome")
