k = 3
tong = 0

for i in range(0, ...):
    if i % 3 != 0:
        tong += i
        dem += 1
        
    if dem == k: break
    
print(tong/dem)