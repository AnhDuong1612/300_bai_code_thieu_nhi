k = int(input())

block = (k - 1) // 2
if k % 2 == 1:
    print(9 * block + 3)
else:
    print(9 * block + 6)