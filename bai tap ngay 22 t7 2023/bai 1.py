import math

# function tìm số nguyên tố
def prime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    for i in range (2, int(sqrt_n) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập N (số lượng phần tử trong mảng): "))

# nhập số vào mảng
arr = []
for i in range(n):
    arr.append(int(input("Nhập số: ")))

# thêm các số nguyên tố vào một list
prime_l = []
for n in arr:
    if prime(n):
        prime_l.append(n)

print("Mảng số nguyên tố:", prime_l)
print("Tổng các số nguyên tố trong mảng:", sum(prime_l))

print()
print("----------")
print()

# nhập số K và tìm index của phần tử = K
k = int(input("Nhập số K: "))

if k in arr:
    print(f"Index của số {k} trong mảng là:",arr.index(k))
else:
    print("Số K không có trong mảng.")
print()
print("----------")
print()

# thêm X vào vị trí Y trong mảng
lst = [1, 2, 3, 4]
print("Mảng:", lst)

x = int(input("Nhập số X: "))
y = int(input("Nhập vị trí Y: "))
lst.insert(y, x)

print("Mảng mới:", lst)