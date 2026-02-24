k = int(input())
def solve(k):
    # Tìm n sao cho có đúng k số không chia hết cho 3
    n = k + (k - 1) // 2
    
    # Tổng từ 1 → n
    total_all = n * (n + 1) // 2
    
    # Số lượng số chia hết cho 3
    m = n // 3
    
    # Tổng các số chia hết cho 3
    total_div3 = 3 * m * (m + 1) // 2
    
    # Tổng k số không chia hết cho 3
    total = total_all - total_div3
    
    average = total / k
    
    return average
print(solve(k))