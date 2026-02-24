i = 0
tong = 0
dem = 0
k = 3
while True:
    if i % 3 != 0:
        tong += i
        dem += 1
    
    print(i)
    i += 1
    if dem == k:
        break
    
print(tong/dem)