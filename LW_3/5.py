stringg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuplee = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a = dir(stringg)
b = dir(tuplee)
for i in range(len(a)):
    if a[i] not in b:
        print(a[i])
print("____________________________________")
for i in range(len(b)):
    if b[i] not in a:
        print(b[i])
