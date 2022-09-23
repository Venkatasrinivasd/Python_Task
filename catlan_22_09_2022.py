n = int(input("enter a number: "))
c = [0 for i in range(n + 1)]
c[0] = c[1] = 1
for i in range(2, n + 1):
    c[i] = 0
    for j in range(i):
        c[i] += c[j] * c[i-j-1]
        c.append(c[i])
print(c[n])
